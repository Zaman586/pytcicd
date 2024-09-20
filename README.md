# Simple Python App with CI/CD Pipeline

This is a simple Python application demonstrating the setup of a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions. The pipeline includes stages for linting, testing, building, and deployment.

## Features

- **Python app**: A simple function to add two numbers.
- **Unit tests**: Basic unit tests using the `unittest` framework.
- **Linting**: Code quality is checked using `flake8`.
- **CI/CD Pipeline**: Automatically triggered on push and pull requests to the `main` branch.

## Project Structure

simple-python-app/ │ ├── app.py # Main application file ├── test_app.py # Unit tests ├── requirements.txt # Dependencies (optional) ├── .github/ │ └── workflows/ │ └── ci.yml # GitHub Actions workflow for CI/CD └── README.md # Project documentation

markdown
Copy code

## Getting Started

### Prerequisites

To run the application locally, you'll need:

- Python 3.x
- Git (for version control)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/simple-python-app.git
   cd simple-python-app
Set up a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the App
You can run the application by executing:

bash
Copy code
python app.py
Running Tests
To run the unit tests, use the following command:

bash
Copy code
python -m unittest discover
Linting
To check the code quality using flake8, run:

bash
Copy code
flake8 app.py
CI/CD Pipeline
The project includes a GitHub Actions workflow that performs the following tasks:

Lint: Checks code quality using flake8.
Test: Runs unit tests using unittest.
Build: Simulates building the application.
Deploy: Placeholder for deployment (currently just an echo, can be customized).
Triggering the Pipeline
The pipeline is triggered on:

Every push to the main branch.
Every pull request targeting the main branch.
To see the workflow in action, check the Actions tab in your repository.

