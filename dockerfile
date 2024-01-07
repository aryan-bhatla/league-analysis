# Use official Docker Python 3.9.7 image as base image
FROM python:3.9.7

# Move to /app directory in container 
WORKDIR /app

# Copy requirements file in local directory to /app directory in container 
ADD ./requirements.txt /app/requirements.txt

# Install requirements for packages in container
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    gfortran \
    libblas-dev \ 
    libc-dev \
    libffi-dev \
    liblapack-dev \ 
    libssl-dev \
    python3-dev 

# Upgrade pip in container 
RUN pip install --upgrade pip

# Pip install required packages in container
RUN pip3 install --user -r requirements.txt 

# Set the PATH in container to include the '/root/.local/bin' directory where f2py is installed 
ENV PATH="/root/.local/bin:${PATH}"

# Copy everything in local directory to /app directory in container 
ADD . /app

# Expose Streamlit port in container (this is purely convention - doesn't actually open the port)
EXPOSE 8501

# Run the application in container
CMD ["streamlit", "run", "app.py"]