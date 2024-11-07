# Using a base image with Python
FROM python:3.9-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file to the container and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copying the rest of the application code to the container
COPY . /app

# Running the QR code generation script
CMD ["python", "generate_qr.py"]
