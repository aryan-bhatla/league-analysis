# Official Docker 3.9.7 base image
FROM python:3.9.7

# Move to /app directory inside container 
WORKDIR /app

# Collect and install packages 
ADD ./requirements.txt /app/requirements.txt

# Add everything in current directory to /app directory in container 
ADD . /app

# Run the application from the container
CMD [ "python", "main.py" ]