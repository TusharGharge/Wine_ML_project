from src.Wine_ml.config.configuration import ConfigurationManager
from src.Wine_ml.components.model_training import ModelTrainer
from src.Wine_ml.utils import logger


STAGE_NAME="Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()