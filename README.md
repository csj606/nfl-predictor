# nfl-predictor - In Progress
This is a web application which uses a random forest regression model to predict NFL score spreads. The application displays the predicted score differential for a game depending on the most recent team statistics for each side.

### Application Structure and Features:

Currently, the following page are being included as a MVP:

- A home page where the games currently being played this week are displayed, along with the predicted score

More pages may be added at a later date, such as player statistics or other models linked to fantasy football.

### Stack:

- Frontend: TypeScript + React components
- Backend: AWS Lambda Functions written in Python, powered by AWS API Gateway
- Database: Amazon DynamoDB
- CI/CD pipeline: GitHub Actions, ECR, ECS
- Testing frameworks: PyTest and Selenium
- ML Model: Random forest model using Scikit-Learn
- IaC: Terraform

### Infrastructure:

- AWS Lambdas and API Gateway for backend services
- Cloudflare Pages and Workers for distributing the frontend and providing some security services
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
