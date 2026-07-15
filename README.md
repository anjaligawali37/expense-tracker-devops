# 💰 Expense Tracker - CI/CD Pipeline with Jenkins, Docker & AWS

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Docker](https://img.shields.io/badge/Docker-2496ED)
![Jenkins](https://img.shields.io/badge/Jenkins-CI-red)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A Django-based **Expense Tracker** application demonstrating an end-to-end **CI/CD pipeline** using **GitHub, GitHub Webhooks, Jenkins, Docker, Docker Hub, Docker Compose, and AWS EC2**.

---

# 🎯 Project Objective

Build and deploy a Django application using an automated CI/CD pipeline where every push to the **main** branch automatically triggers Jenkins to build, push, and deploy the latest version on an AWS EC2 instance.

---

# 🏗️ CI/CD Architecture

<p align="center">
  <img src="images/architecture.png" alt="CI/CD Architecture" width="850"/>
</p>

---

# 🌐 Live Demo

Application URL

```
http://YOUR-EC2-PUBLIC-IP:8000
```

> Replace `YOUR-EC2-PUBLIC-IP` with your AWS EC2 public IP.

---

# 🚀 Features

- User Registration & Login
- Add Expenses
- View Expenses
- Dockerized Django Application
- Automated CI/CD Pipeline
- GitHub Webhook Integration
- Docker Hub Integration
- AWS EC2 Deployment
- Automatic Deployment after every Git Push

---

# 🛠️ Tech Stack

- Python
- Django
- SQLite
- Docker
- Docker Compose
- Jenkins
- Git
- GitHub
- GitHub Webhooks
- Docker Hub
- AWS EC2
- Ubuntu Linux

---

# 📂 Project Structure

```text
expense-tracker-devops/
│
├── accounts/
├── config/
├── dashboard/
├── expenses/
├── templates/
├── images/
│   ├── architecture.png
│   ├── jenkins-success.png
│   ├── webhook-success.png
│   ├── docker-ps.png
│   └── expense-tracker.png
│
├── Dockerfile
├── docker-compose.yaml
├── Jenkinsfile
├── requirements.txt
├── manage.py
└── README.md
```

---

# 📋 Prerequisites

- Python 3.10+
- Docker
- Docker Compose
- Jenkins
- Git
- AWS EC2 (Ubuntu)
- Docker Hub Account

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/anjaligawali37/expense-tracker-devops.git

cd expense-tracker-devops
```

Build the Docker image

```bash
docker build -t expense-tracker .
```

Run the application

```bash
docker compose up -d
```

Open

```
http://localhost:8000
```

---

# ⚙️ CI/CD Workflow

```text
Developer
      │
      ▼
Git Commit & Push
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Webhook
      │
      ▼
Jenkins Pipeline
      │
      ├── Clone Repository
      ├── Build Docker Image
      ├── Push Image to Docker Hub
      ├── Stop Existing Container
      └── Deploy Latest Container
      │
      ▼
AWS EC2 Instance
      │
      ▼
Expense Tracker Application
```

### Workflow Steps

1. Developer pushes code to GitHub.
2. GitHub Webhook automatically triggers Jenkins.
3. Jenkins clones the latest source code.
4. Jenkins builds a Docker image.
5. Jenkins pushes the Docker image to Docker Hub.
6. Jenkins deploys the latest image using Docker Compose.
7. The updated Expense Tracker application is automatically available on AWS EC2.

---

# 🐳 Docker

### Build Image

```bash
docker build -t expense-tracker .
```

### Run Container

```bash
docker run -d -p 8000:8000 expense-tracker
```

### Docker Compose

```bash
docker compose up -d
```

---

# 🚀 Jenkins Pipeline Stages

- Clone Source Code
- Build Docker Image
- Push Image to Docker Hub
- Deploy using Docker Compose

---

# ☁️ Deployment

The application is deployed on an **AWS EC2 Ubuntu Instance**.

Deployment is fully automated using:

- GitHub
- GitHub Webhooks
- Jenkins
- Docker
- Docker Hub
- Docker Compose

Whenever code is pushed to the **main** branch:

1. GitHub sends a webhook request to Jenkins.
2. Jenkins automatically starts the CI/CD pipeline.
3. Docker builds a new application image.
4. The image is pushed to Docker Hub.
5. Docker Compose stops the old container.
6. Docker Compose deploys the latest container.
7. The updated application becomes available on AWS EC2.

---

# 📸 Screenshots

## CI/CD Architecture

![Architecture](images/architecture.png)

---

## Jenkins Pipeline Success

![Jenkins Pipeline](images/jenkins-success.png)

---

## GitHub Webhook

![Webhook](images/webhook-success.png)

---

## Docker Container Running

![Docker](images/docker-ps.png)

---

## Running Application

![Expense Tracker](images/expense-tracker.png)

---

# 📖 Learning Outcomes

Through this project, I gained practical experience with:

- CI/CD Pipeline Implementation
- Jenkins Automation
- GitHub Webhooks
- Docker & Docker Compose
- Docker Hub Integration
- AWS EC2 Deployment
- Linux Administration
- Django Application Deployment
- Git & GitHub Workflow

---

# 🔮 Future Improvements

- Add Nginx Reverse Proxy
- Use PostgreSQL Database
- Integrate Kubernetes
- Configure HTTPS using Let's Encrypt
- Add Monitoring with Prometheus & Grafana
- Deploy using Terraform

---

# 👩‍💻 Author

**Anjali Gawali**

📌 GitHub  
https://github.com/anjaligawali37

📌 LinkedIn  
https://www.linkedin.com/in/anjali-gawali-248b2a399/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
