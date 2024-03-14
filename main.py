import tensorflow as tf # for loading model 
import numpy as np # for array conversion
from PIL import Image as PILImage # for converting an image to pil image format
import cv2 # for image configuration
from tensorflow.keras.models import load_model ,Model

from fastapi import FastAPI, File, UploadFile, Request
# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse



app = FastAPI() # instance of FastAPI class

# mount static folder files to /static route
app.mount("/static",StaticFiles(directory="static"),name="static")


# loading the saved model
model = tf.keras.models.load_model("model/n_wc_model.keras")

# sets the templates folder for the app
templates = Jinja2Templates(directory="template")








@app.get("/",response_class=HTMLResponse)
async def base(request: Request):
	"""
    Function to render `base.html` at route '/' as a get request
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `base.html`
    """
	return templates.TemplateResponse("base.html",{"request":request})








@app.post('/home')
async def home(request: Request):
    """
    Function to render `base.html` at route '/home'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `base.html`
    """

    redirect_url = request.url_for('base')    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)







@app.post("/classify", response_class=HTMLResponse)
async def predictor(request: Request):

	"""
    Function to render `classifier.html` at route '/classify'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `classifier.html`
    """
	
	return templates.TemplateResponse("classifier.html",{"request":request})









@app.post("/describe", response_class=HTMLResponse)
async def describer(request: Request):

    """
    Function to render `describer.html` at route '/describe'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `describer.html`
    """

    return templates.TemplateResponse("describer.html",{"request":request})








@app.post("/about", response_class=HTMLResponse)
async def about(request: Request):
    
     """
    Function to render `about.html` at route '/about'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `about.html`
    """
     return templates.TemplateResponse("about.html",{"request":request})








@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):

    """
    Function to render `classifier.html` at route '/upload'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `classifier.html`
    """


    contents = await file.read()                       # Read the contents of the uploaded file
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)        # Decode the image

    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, [-1, 224, 224,3])            # resizes it to fit the input layer of our classifier model
    result = model.predict(img)                        # and predicts using the model
    response = (
        "The waste in the image is -> Recyclable"
        if result > 0.5
        else "The waste in the image is -> Organic"
    )
   
    

    return templates.TemplateResponse(
        "classifier.html",context = {"request":request,"prediction":response}
        )








import os 

import google.generativeai as genai # our describer AI

from IPython.display import Image as IPImage # to convert image into ipython format


def Describe_image(img):
    
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY")) 
    model = genai.GenerativeModel(model_name = 'gemini-pro-vision',
                                 safety_settings = None,
                                 generation_config = None
                                 )

    pil_img = IPImage(img)
    response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a very short description, about 15 words maximum, of the waste in the photo and classify it as either Organic or Recyclable waste.", pil_img], stream=True)
    response.resolve()
    return response.text
    

@app.post("/descimg", response_class=HTMLResponse)
async def descimg(request: Request, file: UploadFile = File(...)):

    """
    Function to render `describer.html` at route '/describeimg'
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `describer.html`
    """

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)  # Read content and store it as array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)   # Decode the image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Converting image to colour(BGR) format
            


    pil_image = PILImage.fromarray(img) # convert it to Pil image
    pil_image.save('output.png') 
    ''' to temporarily save image and read from it, this is because unless 
        locally stored images can't be read by IPython.Image, here IPImage'''

    response = Describe_image('output.png')
   

    return templates.TemplateResponse(
        "describer.html",context = {"request":request,"prediction":response}
        )

