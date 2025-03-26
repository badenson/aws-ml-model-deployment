# 🚀 AI/ML Model Deployment on AWS

Deploy machine learning models as scalable APIs using AWS serverless technologies. This project demonstrates a production-ready pipeline for hosting, serving, and maintaining ML models in the cloud.

## 🔧 Tech Stack

| Service          | Purpose                          |
|------------------|----------------------------------|
| **Amazon SageMaker** | Model training and hosting       |
| **AWS Lambda**      | Serverless inference layer       |
| **API Gateway**     | REST API endpoint for predictions|
| **Amazon S3**       | Model artifact storage           |
| **SageMaker Pipelines** | Automated model retraining     |

## ✨ Key Features

✅ **End-to-end ML deployment pipeline**  
✅ **Scalable serverless architecture**  
✅ **Automated model updates**  
✅ **Secure REST API endpoints**  
✅ **Cost-effective inference**  

## 📂 Project Structure
aws-ml-model-deployment/
├── infrastructure/
│ ├── sagemaker_model.yml # SageMaker CF template
│ ├── api_gateway.yml # API Gateway config
│ └── lambda_inference.yml # Lambda deployment
├── src/
│ ├── model/ # Training code
│ │ ├── train.py
│ │ ├── requirements.txt
│ │ └── deploy_model.py
│ ├── lambda/ # Inference code
│ │ ├── inference.py
│ │ └── requirements.txt
│ └── scripts/ # Deployment scripts
│ ├── deploy.sh
│ └── update_model.sh
├── docs/
│ ├── architecture.md # System design
│ └── api_spec.md # API documentation
└── README.md


## 🛠️ Deployment Guide

### Prerequisites
- AWS Account with admin permissions
- AWS CLI configured
- Python 3.8+
- Trained ML model (or use our sample)

🏗️ Architecture Overview
graph TD
    A[Client] --> B[API Gateway]
    B --> C[Lambda]
    C --> D[SageMaker Endpoint]
    D --> E[ML Model]
    F[S3 Bucket] --> E
    G[SageMaker Pipeline] --> F

🧩 What You've Built
Component	Description
SageMaker Model	Hosts trained ML model with auto-scaling
Lambda Function	Processes requests and manages inference
API Gateway	Secure HTTPS endpoint for predictions
SageMaker Pipelines	Automated retraining workflow

### 1. Deploy Infrastructure
```bash
./src/scripts/deploy.sh