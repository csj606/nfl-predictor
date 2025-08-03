# nfl-predictor - In Progress
Web Application using ML to predict NFL games and scores

### Application Structure and Features:

The application will consist of five core pages

- A home page where the games currently being played this week are displayed, along with the predicted score
- A page where a user can search for specific teams and view details about them
- A page where a user can make their own predictions against the model and their friends
- A page where a user can see overall global rankings of an individual
- A page where a user can manage and invite people into their fantasy football leagues

### Stack:

- Frontend: TypeScript + React components
- Backend: Django
- Database: Amazon DynamoDB, PostgreSQL
- CI/CD pipeline: GitHub Actions, GitHub Container Registry, Argo CD
- Testing frameworks: PyTest and Selenium
- ML Model: Random forest model using Scikit-Learn

- Authorization and authentication will be handled using built-in features of Django when relevant.
- Terraform scripts will be written to provide a cloud-native version of this application, as well as an Ansible script for on-premise deployment. The entirety of the application will be containerized for ease of use.

### Data Sources:

This is a list of data sources used throughout the project. I will update the list as I add more data to the models.

- pro-football-reference.com
- ESPN

### Repository Structure:
- ./NFLDisplay: contains the Django backend code
- ./Frontend: contains the React + TypeScript frontend code. This will eventually be duplicated to be served out in the ./NFLDisplay directory
- ./ML_Model: contains all of the code and data related to the ML model powering the platform
- ./Infrastructure: contains the Terraform scripts to deploy the relevant AWS infrastructure
- ./DatabaseScripts: contains some SQL commands to set up an on-prem database. May remove this since I'm now more focused on the cloud deployment
