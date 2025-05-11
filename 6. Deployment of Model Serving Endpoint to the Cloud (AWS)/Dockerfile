# Python image
FROM python:3.9-slim

# Working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Expose port 8080 for SageMaker
EXPOSE 8080

# Start the Flask app using Gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "predictor:app"]