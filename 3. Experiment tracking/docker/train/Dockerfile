FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application sub-directories into the container at /app
COPY data_process/ /app/data_process/
COPY models/ /app/models/
# Note: Data will be mounted via docker-compose volume

# Expose port 5005
EXPOSE 5005

# Command to execute the processing and training scripts
# Each script is run sequentially, ensuring that each step is completed before the next begins
CMD python3 data_process/data_manipulation.py && \
    python3 data_process/data_visualization.py && \
    python3 models/lasso_regression.py && \
    python3 models/decision_tree_regression.py && \
    python3 models/linear_regression.py && \
    python3 models/random_forest_regression.py