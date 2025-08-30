# nfl-predictor - In Progress
This is a web application which uses a random forest regression model to predict NFL score spreads. You can also navigate to pages for each specific team, where you can view statistics specific to the team that the model is using.

### Application Structure and Features:

Currently, the following pages are being included as a MVP prior to the start of the 2025 NFL season:

- A home page where the games currently being played this week are displayed, along with the predicted score
- A page where a user can search for specific teams and view details about them

More pages may be added at a later date, such as player statistics or other models linked to fantasy football.

### Stack:

- Frontend: TypeScript + React components
- Backend: Django
- Database: Amazon DynamoDB
- CI/CD pipeline: GitHub Actions, ECR, ECS
- Testing frameworks: PyTest and Selenium
- ML Model: Random forest model using Scikit-Learn
- IaC: Terraform

### Infrastructure:

- A Django backend, a Redis cache, and other containerized backend services
- Cloudflare Pages and Workers for distributing the frontend and providing some security services
- AWS Lambdas and EventBridge Scheduler for dataflows
- Route 53 for DNS services
- DynamoDB tables for our data
- ECR for storing Docker containers, ECS for orchestrating them using Fargate

### Data Sources:

This is a list of data sources used throughout the project. I will update the list as I add more data to the models.

- ESPN
- nfl-verse (data licensed under the MIT license)

### Repository Structure:
- ./NFLDisplay: contains the Django backend code
- ./Frontend: contains the React + TypeScript frontend code.
- ./ML_Model: contains all of the code and data related to the ML model powering the platform
- ./Infrastructure: contains the Terraform scripts to deploy the relevant AWS infrastructure
- ./LambdaScripts: contains the Dockerfiles and Python code for the data pipelines
