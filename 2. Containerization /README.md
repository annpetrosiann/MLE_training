# Data Science project with Docker

This project demonstrates setting up a Docker-based environment for training and inference using logistic regression on the Iris dataset. The setup ensures proper data management, including how to mount data with correct [permissions](https://vsupalov.com/docker-shared-permissions/), and outlines the entire process from data preprocessing and model training to performing inference.

## Project Structure
```
├── data                      # Data files used for training and inference (it can be uploaded with data_upload.py script)
│   ├── train.csv
│   └── test.csv
├── data_process              # Script used for data processing
│   ├── data_upload.py  
├── train                     # Script and Dockerfile used for training
│   ├── Dockerfile
│   ├── train.py     
├── inference                 # Script and Dockerfiles used for inference
│   ├── Dockerfile
│   ├── inference.py
├── saves_model               # Folder where trained model are stored (it can be uploaded with train.py script)
│   └── model.joblib
├── requirements.txt          # List of dependencies required to run the project.
└── README.md
```

## Data

The Iris Flower Dataset is a classic dataset from the field of machine learning, which can be accessed via [this Wikipedia link](https://en.wikipedia.org/wiki/Iris_flower_data_set). It consists of 150 samples from three species of Iris (Iris setosa, Iris virginica, and Iris versicolor). Each sample includes four features: the lengths and the widths of the sepals and petals. This dataset is commonly used for classification problems.

`data_upload.py` script  automatically downloads the Iris dataset from the `scikit-learn` library, and splits it into training and inference datasets to prevent data leakage. 

After running the `data_upload.py` script, a directory named `data` will be created in `2. Containerization `  directory. This folder contains two CSV files:
- `train.csv`: This file holds the training dataset used for building and training the model.
- `test.csv`: This file is used for model testing to ensure that the model performs well on unseen data.

This step ensures that all datasets are prepared and stored separately. 

## Training and Predictions
For this project, since it's a classification task, we went with logistic regression due to its effectiveness. We set `max_iter = 50`, trained our model, and then saved it in the `saved_model` directory using joblib. After that, we loaded the trained model and made predictions on unseen data.
 
## Setup and Running

To run the project, you have two options: locally or using Docker. Below are the steps for each method.

### Local 
1. **Create a virtual environment**:
   ```bash
    python3 -m venv {virtual_environment_name}
   ```
2. **Activate the virtual environment**:
    - On Windows:
      ```bash
      {virtual_environment_name}\Scripts\activate
      ```
    - On macOS or Linux:
      ```bash
      source {virtual_environment_name}/bin/activate
      ```
3. **Install Dependencies**
    ```bash
     pip install -r requirements.txt
     ```
4. **Run the Data uploading Script**
    ```bash
      python3 data_process/data_upload.py
    ```
5. **Run the Training Script**
     ```bash
     python3 train/train.py
     ```
6. **Run the Inference Script**
     ```bash
     python3 inference/inference.py 
     ```

### Docker 

#### **Data uploading**

First, we build the Docker image for data uploading. This step ensures that no cache is used and everything is fresh.

  ```bash
    docker build --no-cache -t data_uploading -f data_process/Dockerfile .
  ```  
Next, we run a container from the built image. This container mounts the local `./data` directory to `/app/data` inside the container. Here, you can interact with the container:
  ```bash
    docker run -it --name data_upload_cont -v ./data:/app/data data_uploading /bin/bash
  ```
Inside the container, list the contents:
   ```bash
     ls
   ```
You will see the `data`, `data_upload.py`, and `requirements.txt` files. The `data` directory will be empty initially. To populate it, run:
 ```bash
   python3 data_upload.py
 ```
After the script runs, the `data` directory will have the necessary datasets. Use the `exit command` to leave the container.
#### **Data training**
Build the Docker image for training without using cache.

``` bash
    docker build --no-cache -t training -f train/Dockerfile .
```
Run a container for training. This mounts `./data` and `./saved_model` to their respective paths in the container.
``` bash
    docker run -it --name training_cont -v ./data:/app/data -v ./saved_model:/app/saved_model training /bin/bash
```
List the contents inside the container:
```bash
  ls
```
You will see the `data` directory with train and test CSVs, and an empty `saved_model` directory,`requirements.txt` and `train.py`. Run the training script:
```bash
  python3 train.py
```
This script trains the model and saves it in the `saved_model` directory. To leave the container use `exit` command.
#### **Model Inference**
Build the Docker image for inference without using cache.

``` bash
    docker build --no-cache -t inference -f inference/Dockerfile .
```
Run a container for inference, similarly mounting the  `data` and `saved_model` directories:
```bash
  docker run -it --name inference_cont -v ./data:/app/data -v ./saved_model:/app/saved_model inference /bin/bash
```
List the contents to verify:
```bash
  ls
```
You'll see `data` directory, `inference.py`, `requirements.txt`, and `saved_model` directory. The `saved_model` directory contains the trained model. Run the inference script:

```bash
  python3 inference.py
```
After making predictions on unseen data, you can leave the container.


These steps ensure that your Docker environment is set up correctly, and each component functions as intended.
### Docker Commands Used in This Project

```bash
   docker build --no-cache -t [image_name] -f [path_to_dockerfile] .
```
`--no-cache` ---> This option tells Docker to build the image without using any cache from previous builds of the same Dockerfile.

`-t` ---> This option specifies the tag (-t) for the image that you are building.

`-f` ---> Specifies the location of the Dockerfile.

```bash
  docker run -it --name [container_name] -v [host_path]:[container_path] [image_name] /bin/bash
```
`-it` ---> This option combines two separate options: `-i` and `-t`. The `-i (--interactive)` option keeps the standard input (stdin) open even if not attached, and the `-t (--tty)` allocates a pseudo-TTY, which provides a terminal interface inside the container. Together, these make the container start in an interactive mode with a terminal attached, suitable for interactive processes like a shell.

`--name` ---> Assigns a name to the container.

`-v`--->  This option mounts a volume from the host machine to the container. It follows the format `host_path:container_path`.

`/bin/bash`--->  This is the command that will be executed inside the container once it starts. In this case, it's running the Bash shell.

# The End