FROM python:3.10.0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install opencv-python-headless==4.5.3.56
EXPOSE $PORT
CMD uvicorn --workers=4 --host 0.0.0.0$PORT main:app
