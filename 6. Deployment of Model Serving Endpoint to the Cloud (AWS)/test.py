import boto3
import json


endpoint_name = "sagemaker-inference-endpoint"

# Input features to test
payload = {
    "features": [7.5, 5.0, 4.0, 1.0]
}

# Create SageMaker runtime client
client = boto3.client("sagemaker-runtime", region_name="eu-north-1")

# Invoke the endpoint
response = client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/json",
    Body=json.dumps(payload)
)

# Read and print result
result = response["Body"].read()
print("Prediction result:", result.decode())
