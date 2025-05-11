# Dockerfile for data uploading
FROM python:3.11

# Set a non-root user
RUN useradd -ms /bin/bash user
USER user

WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY /data_process/data_upload.py /app/