#!/bin/bash

# Deploy SageMaker Model
aws cloudformation deploy --template-file infrastructure/sagemaker_model.yml --stack-name ml-model-stack

# Deploy Lambda
aws cloudformation deploy --template-file infrastructure/lambda_inference.yml --stack-name lambda-stack

# Deploy API Gateway
aws cloudformation deploy --template-file infrastructure/api_gateway.yml --stack-name api-gateway-stack

echo "Deployment complete!"