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
- CI/CD pipeline: GitHub Actions, GitHub Container Repository, Argo CD
- Testing frameworks: PyTest and Selenium
- ML Model: Random forest model using Scikit-Learn

- Authorization and authentication will be handled using built-in features of Django when relevant.
- Terraform scripts will be written to provide a cloud-native version of this application, as well as an Ansible script for on-premise deployment. The entirety of the application will be containerized for ease of use.

### Data Sources:

This is a list of data sources used throughout the project. I will update the list as I add more data to the models.

- pro-football-reference.com
- ESPN
