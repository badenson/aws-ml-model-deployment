#!/bin/bash

# Trigger SageMaker Pipeline
aws sagemaker start-pipeline-execution \
  --pipeline-name "ml-model-retraining" \
  --pipeline-execution-display-name "Model-Retraining-$(date +%Y%m%d)"