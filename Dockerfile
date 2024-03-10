FROM python:3.10.0
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install opencv-python-headless
RUN pip3 install numpy
EXPOSE $PORT
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

