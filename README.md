# 🚀 Flask CI/CD App with GitHub Actions, Docker & Minikube

This project demonstrates a complete CI/CD pipeline using **GitHub Actions**, **Docker**, and **Kubernetes via Minikube**, with a sample **Flask application**.  
The pipeline performs automated testing, Docker image builds, image pushing to Docker Hub, and simulated deployments.

---

## 🧱 Tech Stack

- **Flask (Python 3.10)** – Minimal REST API with `/` and `/health`
- **Docker & Docker Compose** – Containerize and manage the app
- **GitHub Actions** – CI for testing & building Docker image, CD on release
- **Docker Hub** – For image storage & versioning
- **Minikube** – Local Kubernetes deployment (optional)

---

## 📁 Project Structure

ci-cd-app/
├── app/
│ ├── app.py # Flask API
│ ├── requirements.txt # Dependencies
│ └── test_app.py # Basic health check test
├── Dockerfile # Docker build instructions
├── deployment.yaml # Kubernetes Deployment (Minikube)
├── service.yaml # Kubernetes Service (Minikube)
├── .github/
│ └── workflows/
│ ├── ci.yml # CI Workflow (test + build + push)
│ └── cd.yml # CD Workflow (release trigger)
├── screenshots/ # Screenshots of CI/CD & running app
└── README.md # This file


### 🐳 Run with Docker (Locally)
```bash
docker build -t flask-ci-cd .
docker run -p 5000:5000 flask-ci-cd
docker-compose up --build


🌐 Access the App
http://localhost:5000

http://localhost:5000/health

