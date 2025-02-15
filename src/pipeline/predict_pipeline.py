import joblib 
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        # Update the path to the correct location of the model.joblib file
        self.model = joblib.load(Path('e:/Wine Quality Predicition/artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction