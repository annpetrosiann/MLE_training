FROM python:3.9-slim

# Install MLflow
RUN pip install mlflow==2.20.1

# Create mlruns directory (will be mounted from host)
RUN mkdir -p /mlflow/mlruns

# Set the working directory to /mlflow
WORKDIR /mlflow

# Expose port 5005 for the MLflow server
EXPOSE 5005

# --host 0.0.0.0 makes the server available on all network interfaces
# --port 5005 specifies the port on which the server will listen
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5005"]