import os
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    train_data_path: str
    test_data_path: str

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        try:
            df = pd.read_csv(self.config.raw_data_path)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
        except Exception as e:
            raise CustomException(e, sys)