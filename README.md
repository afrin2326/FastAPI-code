# FastAPI Code Practice

A structured collection of hands-on projects and practical examples built with **FastAPI**, Python, Pydantic, and Machine Learning. This repository documents my learning journey in backend development, RESTful API design, data validation, and machine learning model deployment.

## Overview

This repository contains practical implementations of FastAPI concepts, ranging from fundamental API development to integrating machine learning models into API-based applications. Each project focuses on building a stronger understanding of Python backend engineering and developing reusable, maintainable applications.

## Projects

### 1. CRUD Operations
A practical implementation of Create, Read, Update, and Delete (CRUD) operations using FastAPI.

**Key Concepts**
- Building API endpoints for data management
- Handling HTTP requests and responses
- Working with JSON-based data storage
- Implementing basic backend application logic

### 2. Machine Learning with FastAPI
An example of integrating a machine learning model into a FastAPI application to serve predictions through API endpoints.

**Key Concepts**
- Loading and using a trained machine learning model
- Exposing predictions through API endpoints
- Processing input data for model inference
- Working with a machine learning dataset
- Exploring API-based ML application workflows

### 3. Path Parameters
Practical examples of using path parameters to create dynamic API endpoints.

**Key Concepts**
- Defining dynamic routes
- Extracting values from URL paths
- Handling request parameters
- Building flexible API endpoints

### 4. Pydantic Validation
Examples demonstrating data validation and schema definition using Pydantic.

**Key Concepts**
- Defining data models
- Validating input data
- Using field validators
- Understanding structured data validation

## Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Data Validation:** Pydantic
- **Machine Learning:** Scikit-learn-compatible model workflows
- **Data Formats:** JSON, CSV
- **Development Tools:** Jupyter Notebook, Uvicorn, Git, GitHub

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or a compatible version
- pip
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/afrin2326/FastAPI-code.git
cd FastAPI-code
```

**2. Create a virtual environment**

```bash
python -m venv myenv
```

**3. Activate the virtual environment**

Windows — Command Prompt:

```bash
myenv\Scripts\activate
```

Windows — Git Bash:

```bash
source myenv/Scripts/activate
```

**4. Install dependencies**

Install the packages required by the project you want to run. For example:

```bash
pip install fastapi uvicorn pydantic
```

For the machine learning project, additional dependencies may be required depending on the imports in its Python files:

```bash
pip install pandas numpy scikit-learn
```

## Running the Applications

Navigate to the relevant project directory before running its application.

### CRUD Operations

```bash
cd "CRUD operation"
uvicorn main:app --reload
```

### Machine Learning with FastAPI

```bash
cd "ML model with Fast API"
uvicorn main:app --reload
```

### Path Parameters

```bash
cd "Path params"
uvicorn main:app --reload
```

The commands above assume that each corresponding `main.py` defines a FastAPI instance named `app`. If an application uses a different variable name or entry-point file, adjust the command accordingly.

After starting an application, open the interactive API documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Learning Objectives

Through these projects, I aim to strengthen my understanding of:

- RESTful API development with FastAPI
- HTTP methods and request handling
- CRUD operations and data management
- Path parameters and dynamic routing
- Data validation with Pydantic
- Machine learning model integration with backend services
- Python application structure and API testing

## Future Improvements

- Add automated tests using Pytest
- Introduce a database-backed CRUD implementation
- Add dependency management with a `requirements.txt` file
- Improve error handling and API response consistency
- Add input validation and model evaluation details to the ML application
- Explore authentication, database integration, and API deployment

## About This Repository

This repository serves as a practical learning resource for Python backend development and machine learning integration. It will continue to evolve as I explore additional FastAPI features and build more advanced applications.

## Author

**Mst Afrin Binte Amin**

- GitHub: [@afrin2326](https://github.com/afrin2326)

---

*Built as part of my continuous learning journey in Python, backend engineering, and applied machine learning.*
