# AWS SageMaker Deployment

This project demonstrates how to package and deploy a **pretrained machine learning model** to an **AWS SageMaker endpoint** using a **custom Docker container**.

It includes a simple Flask-based HTTP server for serving predictions, containerized with Docker and deployed to SageMaker for real-time inference.

---

## 📁 Project Structure
````
├── predictor.py
├── test.py                     
├── Dockerfile
├── model.pkl            
├── scaler.pkl      
├── requirements.txt       
└── README.md
````
`predictor.py`: A Flask web server that loads a pretrained model (model.pkl) and a scaler (scaler.pkl).
It responds to:
- `/ping`  for health checks (required by SageMaker)
- `/invocations` receives input data and returns predictions
Converts numerical predictions into labeled strings (e.g., 🌸 Iris-versicolor).

`test.py`: Sends a JSON payload to the deployed SageMaker endpoint using boto3 and the sagemaker-runtime client.
It calls the `/invocations` route and prints the prediction result to the terminal.

`Dockerfile`: Builds a minimal Python-based Docker image.
It copies code and model files into the container, installs Flask, Gunicorn, and required dependencies, and starts the server using Gunicorn on port 8080 (required by SageMaker).

---

## 🧠AWS SageMaker

**AWS SageMaker** is a fully managed service that allows you to build, train, and deploy machine learning models at scale.  
This project focuses **only on deployment**, using a **custom container** that runs a trained model using Flask + Gunicorn.

We used:
- **Amazon ECR (Elastic Container Registry)** to store the Docker image
- **SageMaker Inference** to deploy the container
- **Boto3 (`sagemaker-runtime`)** to call the endpoint

---

## 🛠 Build & Push Docker Image to AWS

### Step 1: Authenticate Docker to AWS ECR

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
```
After running a command, you might see the following message:
`Unable to locate credentials. You can configure credentials by running "aws configure".`

If you're new and don't have any credentials yet, you'll need to generate access keys from the AWS Management Console(see below):

<img width="1196" alt="key1" src="https://github.com/user-attachments/assets/d2f96093-6f8c-479f-9d1c-70aa66ca8c93" />
<img width="1196" alt="key2" src="https://github.com/user-attachments/assets/67a22d03-3098-4a89-9328-db7a3aa855cd" />

Then, configure AWS CLI by running:
```bash
aws configure
```
You'll be prompted to enter AWS Access Key ID, AWS Secret Access Key, Default region name (e.g., us-east-1),Default output format (e.g., json). After completing the configuration, re-run command. You should see `Login Succeeded` message.

### Step 2: Create a Private Repository

Before proceeding, we need to create a repository.

![repo1](https://github.com/user-attachments/assets/a74237e9-db3e-4859-9680-fda4d679d295)
![repo2](https://github.com/user-attachments/assets/8cd9ef31-c6a5-4c96-98eb-533a8018f08b)

Once the repository is created, click on it to open. It will initially be empty.

<img width="1211" alt="image1" src="https://github.com/user-attachments/assets/cc6f99d1-4312-49eb-86d5-e4ac4c7175f6" />

### Step 3: Push Docker Image to ECR
Run the following commands to upload Docker image, then refresh the page:
```bash
# Build the Docker Image for x86_64 (compatible with SageMaker)
docker build --platform linux/amd64 --provenance false -t <image_name> .

# Tag the Image for ECR
docker tag <image_name>:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/<repo_name>:latest

# Push to ECR
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/<repo-name>:latest
````
After the push completes, refresh the repository page. You should now see image listed there.

![image2](https://github.com/user-attachments/assets/a2723b6c-26c9-49e1-bc80-7b7562586362)

---

## 🚀 Deploy in AWS SageMaker Console

From the `Amazon SageMaker` console, go to `Models` and click Create model.
For **Location of inference code image**, provide the **Docker image URI**
(found under ECR repository → Images → Image URI).

![model1](https://github.com/user-attachments/assets/875c3c00-989d-4925-b3fd-9d54befe676d)
![model2](https://github.com/user-attachments/assets/0879cf99-a0e2-499f-8883-cbae4180ad59)


After creating the model, you need to create an `endpoint configuration` and select the model you just created.

![endpoint_config](https://github.com/user-attachments/assets/14d21ddb-0474-47e4-9480-9b83a1cec323)


Once the endpoint configuration is created, go to `Endpoints`, click **Create**, select **Use existing endpoint configuration**, choose the one you just created, and then click **Create**. It will take a few moments for the endpoint status to change to `InService`.  

![endpoint1](https://github.com/user-attachments/assets/a73b6327-4bbd-453a-b105-6ad7ea81f0f1)

Once it’s active, you can go to the terminal and run `test.py`.
You will see the prediction printed in the console.
![test](https://github.com/user-attachments/assets/e13a37d3-da9b-441b-a4de-059d5dfb0459)


*Note: `\ud83c\udf38` is just an emoji that can't be displayed properly in the terminal —ignore it.*

![endpoint2](https://github.com/user-attachments/assets/123a3b78-4a3b-45a4-bc6d-8c3ef571f891)


The endpoint `sagemaker-inference-endpoint` is now InService, meaning it’s ready to receive requests. You can view the model container logs by clicking the link under `Model container logs`. The endpoint currently shows **0 alarms**, indicating it is running without any issues. 
