<div align="center">

# xhec-mlops-project-student

[![CI status](https://github.com/artefactory/xhec-mlops-project-student/actions/workflows/ci.yaml/badge.svg)](https://github.com/artefactory/xhec-mlops-project-student/actions/workflows/ci.yaml?query=branch%3Amaster)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

## Marie-Sophie Richard, Idriss Bennis, Samuel Berredi, Joseph Moussa, Ajouad Akjouj, Mathieu Péharpré

This repository has for purpose to guide you in the use of our industrialized model for the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

**Goal**: predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...)


## Table of Contents

- [Context](#context)
- [Method used](#method-used)
  - [Creation of the environment](#creation-of-the-environment)
  - [EDA](#eda)
  - [Modelling](#modelling)
  - [From notebooks to modules](#from-notebooks-to-modules)
  - [Use prefect](#use-prefect)
  - [Deploy model API](#deploy-model-API)
- [Steps to use and test our code](#steps-to-use-and-test-our-code)

## Context 
The goal of this project is to create both an API and a linked docker image in order to be able to use our model.
A customer wants to be able to predict the age of abalone (column "Rings") from physical measurements ("Shell weight", "Diameter", etc...), thanks to our project he/she will be able to do so and import their own data to make predictions.
This is a way of making a machine learning model available for anyone at anytime without needing to know how to code or how to use a machine learning model.

## Method used 
### Creation of the environment
Creation of a dedicated project environment thanks to a environment.yml file available [here](./environment.yml).  
Creation of a pre-commit document allowing us to test the code using Flake8 and Black at each commit. Code available [here](.pre-commit-config.yaml).  
Creation of a requirements.in doc ([here](./requirements.in) and [here](./requirements-dev.in)) to monitor dependencies and keep track of useful libraries for this project. The document is coupled with a requirements.txt doc ([here](./requirements.txt) and [here](./requirements-dev.txt)).  

### EDA
EDA notebook available [here](./notebooks/eda.ipynb).  
Exploration of the dataset and simple feature engineering to format the dataset.   
Creation of a test and a train set saved in the file .data/raw/...  

### Modelling
Modelling notebook available [here](./notebooks/modelling.ipynb).  
Ridge model finetuned thanks to a gridsearch.   
Results stored and monitored through MLFlow to keep track of the parameters and models tested.  

### From notebooks to modules 
.py documents available [here](./src/modelling).  
Code compiling the notebooks created in the previous step in order to go from notebooks to useful and deployable modules.  
Those .py documents turn the previous notebooks into efficient functions.

### Use prefect
Set an API URL for our local server to make sure that your workflow will be tracked by this specific instance :
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api  
The code used to creat this model can be found [here](./src/modelling).   
Mainly the workflows.py document (available [here](./src/modelling/workflows.py)), creating the worklfow needed for the API by processing the data, training and saving the model.

### Deploy model API
Creation of a model API to be able to use the model in production.  
The code used to created deploy this API can be found [here](./src/web-service).  
Then, we created an app with Docker to be able to deploy the API on a server.  
The code used to create a docker image can be found [here](./Dockerfile.app).

## Steps to use and test our code

In order to set up the necessary libraries and dependencies, first **create a conda environment** for this project, using the following command in your terminal:

```bash
conda create env -f environment.yml
```

Then, **activate the environment**:

```bash
conda activate x-hec-solution
```

Then **train the model**:

```bash
cd src/modelling
python workflows.py
```

Then, you can run the following command to **deploy the API** (without Docker):

```bash
cd src/web_services #GO INTO THE RIGHT FOLDER
uvicorn main:app --reload
```

And then, if your to **create your docker image**, use the following command (in the root folder):

```bash
docker build -t my_docker_image -f Dockerfile.app .
```
