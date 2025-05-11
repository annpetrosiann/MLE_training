# Official Apache Airflow image (version 2.10.5 with Python 3.9)
FROM apache/airflow:2.10.5-python3.9

# Switch to root user to install system packages
USER root

# Update package lists and install Graphviz (used for DAG visualization, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    graphviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Copy Python requirements file to container
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy DAGs into the Airflow DAGs folder inside the container
COPY dags/ /opt/airflow/dags/