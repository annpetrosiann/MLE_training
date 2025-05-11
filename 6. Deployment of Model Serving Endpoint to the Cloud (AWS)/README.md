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


<img width="1196" alt="key1" src="https://github.com/user-attachments/assets/b1d08aba-e39f-4f22-9442-58deea8cf126" />
<img width="1196" alt="key2" src="https://github.com/user-attachments/assets/12f220e6-50be-426e-924d-68f6c4053144" />

Then, configure AWS CLI by running:
```bash
aws configure
```
You'll be prompted to enter AWS Access Key ID, AWS Secret Access Key, Default region name (e.g., us-east-1),Default output format (e.g., json). After completing the configuration, re-run command. You should see `Login Succeeded` message.

### Step 2: Create a Private Repository

Before proceeding, we need to create a repository.

![repo1 23 55 15](https://github.com/user-attachments/assets/68090940-3729-4f5a-b2c1-2a45a08a6249)
![repo2 23 55 15](https://github.com/user-attachments/assets/437a6b05-e8f1-44f6-8804-7a7a2ac3e663)

Once the repository is created, click on it to open. It will initially be empty.

<img width="1211" alt="image1" src="https://github.com/user-attachments/assets/bfecf31d-a5b9-499c-8da2-3af0615089ed" />

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


![image2 23 55 15](https://github.com/user-attachments/assets/01e55faa-7aa8-4690-adc9-1cdaa81e7c54)

---

## 🚀 Deploy in AWS SageMaker Console

From the `Amazon SageMaker` console, go to `Models` and click Create model.
For **Location of inference code image**, provide the **Docker image URI**
(found under ECR repository → Images → Image URI).

![model1 23 55 15](https://github.com/user-attachments/assets/e0bdb584-1246-4833-847c-4b73eba380f5)
![model2 23 55 15](https://github.com/user-attachments/assets/64dc045d-023e-45fe-8322-1a286cc8223d)


After creating the model, you need to create an `endpoint configuration` and select the model you just created.

![endpoint_config 23 55 15](https://github.com/user-attachments/assets/bd8af4ae-203d-456b-bb22-ea83b51e6bc5)

Once the endpoint configuration is created, go to `Endpoints`, click **Create**, select **Use existing endpoint configuration**, choose the one you just created, and then click **Create**. It will take a few moments for the endpoint status to change to `InService`.  

![endpoint1 23 55 15](https://github.com/user-attachments/assets/347e6627-8f9b-4c59-ac6d-6974c4e04ddf)


Once it’s active, you can go to the terminal and run `test.py`.
You will see the prediction printed in the console.

![test 23 55 15](https://github.com/user-attachments/assets/238d3b7f-ac54-4180-a4c8-b8967a890b15)


*Note: `\ud83c\udf38` is just an emoji that can't be displayed properly in the terminal —ignore it.*

![endpoint2 23 55 15](https://github.com/user-attachments/assets/9c805dcc-be9f-47d0-a653-a636a76e705e)



The endpoint `sagemaker-inference-endpoint` is now InService, meaning it’s ready to receive requests. You can view the model container logs by clicking the link under `Model container logs`. The endpoint currently shows **0 alarms**, indicating it is running without any issues. 
