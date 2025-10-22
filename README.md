# nfl-predictor - On Pause
This is a web application which uses a random forest regression model to predict NFL score spreads. The application displays the predicted score differential for a game depending on the most recent team statistics for each side.

### Application Structure and Features:

Currently, the backend and infrastructure is fully constructed, with the model sitting at an accuracy of around 11%. While this could be improved, it would take a significant amount of data, to the point where I've decided to halt work. The frontend is not done, but frankly I've done what I've considered to be the interesting part of the project: the backend. **For obvious reasons, I would also caution against any individual using this model to place bets on NFL games**.

### Stack:

- Frontend: TypeScript + React components
- Backend: AWS Lambda Functions written in Python, powered by AWS API Gateway
- Database: Amazon DynamoDB
- ML Model: Random forest model using Scikit-Learn
- IaC: Terraform

### Infrastructure:

- AWS Lambdas and API Gateway for backend services
- AWS Lambdas and EventBridge Scheduler for data pipelines
- DynamoDB tables for the data
- ECR for storing Docker containers

### Data Sources:

This is a list of data sources used throughout the project. I will update the list as I add more data to the models.

- ESPN
- nfl-verse (data licensed under the MIT license)

### Repository Structure:
- ./Frontend: contains the React + TypeScript frontend code.
- ./ML_Model: contains all of the code and data related to the ML model powering the platform
- ./Infrastructure: contains the Terraform scripts to deploy the relevant AWS infrastructure
- ./LambdaScripts: contains the Dockerfiles and Python code for the data pipelines
