# ModelFlow-CICD-Pipeline

A comprehensive CI/CD pipeline setup for a Flask application, featuring automated testing, Docker containerization, and deployment. Designed to ensure code quality and streamline the development process.....

# FlaskCI-CDPipeline

This repository demonstrates a complete Continuous Integration/Continuous Deployment (CI/CD) pipeline for a Flask-based application. It integrates several modern development tools and practices to ensure a streamlined workflow from development to deployment.   




## Features

- **GitHub Actions**: Automated workflows for code linting with Flake8 and unit testing to ensure code quality and reliability.
- **Docker**: Containerization of the Flask application for consistent environments from development to production.
- **Jenkins**: Automated deployment pipeline that builds Docker images and pushes them to Docker Hub upon changes to the master branch.
- **Automated Notifications**: Configuration to send email notifications to the admin upon successful deployments or failures, ensuring immediate awareness.

## Branching Strategy

- `master`: The production branch that holds the deployment-ready code.
- `dev`: The development branch where new features and fixes are merged and tested.
- `test`: The testing branch used for more rigorous testing before merging into `master`.

## Getting Started

### Prerequisites

- Git
- Docker
- Python 3
- Flask
- Jenkins (with GitHub and Docker plugins installed)

### Setup

**Clone the Repository**
https://github.com/revolutionaryanusha/ModelFlow-CICD-Pipeline.git

**Navigate to the Repository**
cd FlaskCI-CDPipeline

**Install Dependencies**
pip install -r requirements.txt

**Run the Flask Application Locally**
python app.py

## Contributing

To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request targeting the `dev` branch.

<<<<<<< HEAD
trail push 1
=======

<<<<<<< HEAD
#####----------------------------############
=======
trail push 2

>>>>>>> 788b6b40aba1e085aa19b36952934b4f82e7d2b8
>>>>>>> abe1bdb9d6c6efb089f794b935dad5f0d7e4b141
