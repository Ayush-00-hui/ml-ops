# House Price Prediction - ML & MLOps Pipeline

An end-to-end Machine Learning and MLOps pipeline for House Price Prediction using **MLflow**, **Docker**, **Kubernetes (Kind)**, and **Jenkins**.

---

## 📁 Directory Structure

```
mlflow-homeprice/
│
├── data/                       # Dataset & data generation scripts
│   ├── raw/
│   │   └── house_prices.csv    # Primary training dataset
│   └── generate_fake_data.py   # Synthetic data generation utility
│
├── src/                        # Machine Learning source code
│   ├── train.py                # Model training & MLflow tracking script
│   ├── predict.py              # Model inference / evaluation script
│   └── utils/
│       └── pickle_utils.py     # Data pickling utilities
│
├── docker/                     # Docker container configuration
│   ├── Dockerfile              # MLflow model serving image definition
│   └── Dockerfile.jenkins      # Jenkins build context Dockerfile
│
├── k8s/                        # Kubernetes deployment & service manifests
│   ├── deployment.yml          # Kubernetes deployment configuration
│   ├── service.yml             # Kubernetes service configuration
│   └── kind-config.yml         # Kind cluster multi-node configuration
│
├── jenkins/                    # CI/CD Jenkins automation pipelines
│   ├── Jenkinsfile.local       # Local deployment Jenkins pipeline
│   ├── Jenkinsfile.cloud       # Cloud deployment Jenkins pipeline
│   └── README.md               # Jenkins setup and execution guide
│
├── docs/                       # Project documentation & guides
│   ├── Steps-home-mlflow.md    # End-to-end deployment guide
│   ├── WindowsSetup.md         # Windows environment configuration
│   ├── python_notes.md         # Reference programming snippets
│   └── images/                 # Architecture diagrams and screenshots
│
├── mlruns/                     # MLflow experiment runs and artifact store
├── mlflow.db                   # MLflow SQLite backend database
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview & documentation
```

---

## 🚀 Quick Start Guide

### 1. Environment Setup
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Train Model & Track Experiments
```bash
python src/train.py
```

Launch the MLflow UI:
```bash
mlflow ui
# Access UI at http://127.0.0.1:5000
```

### 3. Model Inference
```bash
python src/predict.py
```

### 4. Container Deployment (Docker)
Build and run the Docker container:
```bash
docker build -t house-price:v1 -f docker/Dockerfile .
docker run -d -p 1234:1234 --name house-api house-price:v1
```

Test the API endpoint:
```bash
curl -X POST http://127.0.0.1:1234/invocations \
-H "Content-Type: application/json" \
-d '{
  "dataframe_records": [
    {
      "LotArea": 9000,
      "OverallQual": 7,
      "OverallCond": 5,
      "YearBuilt": 2010,
      "GrLivArea": 1900,
      "GarageCars": 2
    }
  ]
}'
```

### 5. Kubernetes Deployment (Kind)
```bash
kind create cluster --config k8s/kind-config.yml
kind load docker-image house-price:v1
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl port-forward service/house-price-service 8080:80
```

---

## 📄 Additional Documentation
- [End-to-End Setup & Deployment Guide](docs/Steps-home-mlflow.md)
- [Jenkins CI/CD Pipeline Setup](jenkins/README.md)
- [Windows Environment Setup](docs/WindowsSetup.md)
