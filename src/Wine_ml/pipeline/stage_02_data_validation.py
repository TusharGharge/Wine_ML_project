from src.Wine_ml.config.configuration import ConfigurationManager
from src.Wine_ml.components.data_validation import DataValiadtion
from src.Wine_ml.utils import logger


STAGE_NAME='Data Validation stage'


class DataValidationTrainingPipeline:
    def __iniit__(self):
        pass

    def main(self):
       
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>> step {STAGE_NAME} started <<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x=======x")

    except Exception as e:
        logger.exception(e)
        raise e



