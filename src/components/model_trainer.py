import os
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join('artifacts', "model.pkl")
    # Add other configuration parameters as needed

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_trainer(self, train_arr, test_arr):
        # Implement the model training logic here
        pass
