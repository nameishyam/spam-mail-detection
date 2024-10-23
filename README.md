# Email Spam Detection using Machine Learning

This project aims to predict whether an email is spam or not using machine learning algorithms. The web application is built with Flask and deployed using Docker on [Render](https://render.com).

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Model](#machine-learning-model)
- [Docker Deployment](#docker-deployment)
- [Render Deployment](#render-deployment)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview
Spam emails can clutter your inbox, pose security risks, and waste valuable time. This project classifies emails as either *spam* or *not spam* based on their content using machine learning techniques. The Flask app serves a web interface where users can input email text and get predictions.

## Features
- Predict whether an email is spam or not.
- Clean and intuitive web interface built with Flask.
- Dockerized for seamless deployment.
- Hosted and deployed on Render.

## Installation

### Prerequisites
- Python 3.x
- Docker

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/nameishyam/spam-mail-detection.git
    cd spam-mail-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app locally:
    ```bash
    python app.py
    ```

4. To build and run the Docker container:
    ```bash
    docker build -t spam-detection .
    docker run -p 5000:5000 spam-detection
    ```

## Usage
Once the app is running locally or in Docker, navigate to `http://localhost:5000` in your browser. You can input email content and get a prediction (spam or not spam).

## Machine Learning Model
The machine learning model is trained using a dataset of labeled emails. Several algorithms were evaluated, and the best-performing model was selected for this application. The model preprocesses the email content by tokenizing and vectorizing the text before making a prediction.

## Docker Deployment
This project is containerized using Docker for easy deployment. To use the Docker image:
1. Build the image:
    ```bash
    docker build -t spam-detection .
    ```
2. Run the container:
    ```bash
    docker run -p 5000:5000 spam-detection
    ```

## Render Deployment
The application is deployed on Render, a cloud platform that allows for easy deployment of web applications.

To deploy on Render:
1. Push the Dockerized application to your GitHub repository.
2. Link the repository to Render and deploy using Docker.

## Technologies Used
- **Machine Learning**: Scikit-learn, Natural Language Processing
- **Web Framework**: Flask
- **Deployment**: Docker, Render
- **Languages**: Python, HTML, CSS

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
