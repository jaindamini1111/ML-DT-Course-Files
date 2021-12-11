### Problem Statement

Given the increased activity in cyber security space due to malwares etc. we have a internet firewall dataset where we predict if given the information the site should be allowed 
to visit or not.

https://archive.ics.uci.edu/ml/datasets/Internet+Firewall+Data#

https://doi.org/10.1109/ISDFS.2018.8355382


We have the following information:

Table 1. Features and Description. Adapted from Ertam & Kaya, 2018.

![image](https://user-images.githubusercontent.com/39940054/145679023-0e9ea7ae-dcfa-4195-b023-53a83bae5857.png)

Table 2. Classes to predict (Actions). Adapted from Ertam & Kaya, 2018.

![image](https://user-images.githubusercontent.com/39940054/145679047-3bcdc358-d298-4184-824f-dbc0fe806a33.png)


The variable we want to predict is from the action feature.

### How to Run it Locally

EDA is present in notebook

Model training with hyperparamter tuning is also present in the notebook

Exporting notebook to script - train.py

Model deployment is done with Flask - predict.py

Dependency and enviroment management - requirements.txt, pipfile

Containerization - Dockerfile

The environment and dependency manager used in this project is Pipenv. If you don't have it already installed, you can do it 
using (assuming Python is already installed in the system)

`pip3 install pipenv`

If it doens't work, you can try

`pip install pipenv`

Now, at the project directory, we can install the necessary libraries and dependencies from the Pipfile using:

`pipenv install`

If you want to run the notebook, use the following command to install the extra dependencies:

`pipenv install --dev`

Now activate the environment:

`pipenv shell`

if you want to retrain the model and resave the model you can do it by running

`python train.py`

To deploy the Flask app locally and run it directly

`python predict.py`

So, the project should then be running locally at http://localhost:6969

To test the app using a POST request we can upload the `test_firewall.csv`

We can build and run the Docker image locally with the Dockerfile provided.

To build a Docker image called "firewall_prediction":

`docker build -t firewall_prediction .`

To run it:

`docker run -it --rm -p 6969:6969 firewall_prediction`

To test it we can upload the `test_firewall.csv`
