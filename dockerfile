# Use official Docker Python 3.9.7 image as base image
FROM python:3.9.7

# Move to /app directory in container 
WORKDIR /app

# Copy requirements file in local directory to /app directory in container 
ADD ./requirements.txt /app/requirements.txt

# Pip install required packages in container
RUN pip install -r requirements.txt 

# Copy everything in local directory to /app directory in container 
ADD . /app

# Run the application in container
CMD [ "python", "main.py" ]