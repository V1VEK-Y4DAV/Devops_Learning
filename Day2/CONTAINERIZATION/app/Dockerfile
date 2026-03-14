# Use an official Python runtime as a parent image, using a slim variant for a smaller image size
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt ./

# Install the application dependencies
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run the application when the container starts
CMD ["python", "main.py"]
