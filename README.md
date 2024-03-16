# Waste-Classifcation-web-app
Waste Classifier web app is used to predict the type of waste(Organic/Recyclable) from an image. 
Here a pretrianed model-Vgg19B-is trained and fine-tuned for our classfier.</br> We've added another genai feature, Our Image Describer.
We integrated and used google's GeminiAI for our describer module. Later we Dockerized the webapp and deployed it using render Cloud.
Created using python's tensorflow, Fastapi, numpy and joblib packages.

![python 3.11.0](https://img.shields.io/badge/Python-blue.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?logo=TensorFlow&logoColor=white)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?logo=render&logoColor=white)
![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)

## Dataset Description

The dataset consist of two classes, Organic and Recyclable.

The data contains the following columns:

| Feature Name               | Feature Description                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Organic                    | Images of Organic Waste(plants, flower, leaves, etc.)                                               |
| Recyclable                 | Images of Recyclable Waste(paper, plastic, etc.)                                                    |


## Site Link:

https://waste-classifcation-for-optimal-waste.onrender.com/

## Installation

Open Anaconda prompt and create new environment

```
conda create -n your_env_name python = (any_version_number > 3.11.0)
```

Then Activate the newly created environment

```
conda activate your_env_name
```

Clone the repository using `git`

```
git clone gh repo clone Baktho-SN/Waste_Classifcation_for_optimal_waste_management
```

Change to the cloned directory

```
cd <directory_name>
```

To install all requirement packages for the app

```
pip install -r requirements.txt
```

Then, Run the app

```
uvicorn main:app --reload
```

## 📷 Screenshots

### Website

![Homepage1](markdown/Homepage1.png)
![Homepage2](markdown/Homepage2.png)
![Homepage3](markdown/Homepage3.png)
![Classifier](markdown/Classifier.png)
![Describer](markdown/Describer.png)

## Classifier Demo

![Classifier Demo.GIF](markdown/DEMO.webp)

## Describer Demo

![Describer Demo.GIF](markdown/DEMO1.webp)
