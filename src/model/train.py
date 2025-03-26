from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import boto3

# Train a simple model
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)

# Save model locally
joblib.dump(model, "model.joblib")

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file("model.joblib", "your-model-bucket", "iris_model/model.joblib")