import os
import mlflow.pyfunc
import pandas as pd

# Load the MLflow model
model_path = os.path.join(os.path.dirname(__file__), "mlruns", "1", "models", "m-2a4c27becbe64ac2b4e509ac2a34c155", "artifacts")
if not os.path.exists(model_path):
    model_path = "mlruns/1/models/m-2a4c27becbe64ac2b4e509ac2a34c155/artifacts"

model = mlflow.pyfunc.load_model(model_path)

# Sample house data
home = pd.DataFrame([
    {
        "LotArea": 9000,
        "OverallQual": 7,
        "OverallCond": 5,
        "YearBuilt": 2010,
        "GrLivArea": 1900,
        "GarageCars": 2
    }
])

# Predict
prediction = model.predict(home)

print("Predicted House Price:", prediction[0])
