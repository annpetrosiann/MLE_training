# Python base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy project files
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 8080

# Set entrypoint command to run Flask app
CMD ["python", "iris_deploy/rest_server.py"]
