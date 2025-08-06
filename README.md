# nfl-predictor - In Progress
Web Application using ML to predict NFL games and scores

### Application Structure and Features:

Currently, the following pages are being included as a MVP prior to the start of the 2025 NFL season:

- A home page where the games currently being played this week are displayed, along with the predicted score
- A page where a user can search for specific teams and view details about them

As the season is ongoing, the following features will be added on a rolling basis:

- A page where a user can make their own predictions against the model and their friends
- A page where a user can see overall global rankings of an individual
- A page where a user can manage and invite people into their fantasy football leagues

### Stack:

- Frontend: TypeScript + React components
- Backend: Django
- Database: Amazon DynamoDB
- CI/CD pipeline: GitHub Actions, GitHub Container Registry, Argo CD
- Testing frameworks: PyTest and Selenium
- ML Model: Random forest model using Scikit-Learn
- IaC: Terraform

### Infrastructure:

- An AWS EC2 instance for the Django backend, a Redis cache, and other containerized backend services
- An AWS S3 instance for a static frontend
- AWS Lambdas and EventBridge Scheduler for dataflows
- Route 53 for DNS services
- DynamoDB tables for our data

### Data Sources:

This is a list of data sources used throughout the project. I will update the list as I add more data to the models.

- pro-football-reference.com
- ESPN

### Repository Structure:
- ./NFLDisplay: contains the Django backend code
- ./Frontend: contains the React + TypeScript frontend code. This will eventually be duplicated to be served out in the ./NFLDisplay directory
- ./ML_Model: contains all of the code and data related to the ML model powering the platform
- ./Infrastructure: contains the Terraform scripts to deploy the relevant AWS infrastructure
