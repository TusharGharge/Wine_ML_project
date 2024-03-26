from src.Wine_ml.utils import logger
from src.Wine_ml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Wine_ml.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Wine_ml.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Wine_ml.pipeline.stage_04_model_train import ModelTrainerTrainingPipeline
from src.Wine_ml.pipeline.stage_05_model_evalution import ModelEvaluationTrainingPipeline
STAGE_NAME='Data Ingestion stage'

if __name__ == '__main__':
    try:
        logger.info(f">>>>> step {STAGE_NAME} started <<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x=======x")

    except Exception as e:
        logger.exception(e)
        raise e

    try:
        logger.info(f">>>>> step {STAGE_NAME} started <<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x=======x")

    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

    STAGE_NAME = "Model Training stage"

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = ModelTrainerTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Model Evalution stage"

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = ModelEvaluationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    

    
