import json
import boto3
import joblib
import os

sagemaker = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    # Get input data from API Gateway
    input_data = json.loads(event["body"])
    
    # Call SageMaker endpoint
    response = sagemaker.invoke_endpoint(
        EndpointName="iris-classifier-endpoint",
        ContentType="application/json",
        Body=json.dumps(input_data)
    
    # Return prediction
    prediction = json.loads(response["Body"].read().decode())
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": prediction})
    }