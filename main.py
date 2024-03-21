from src.Wine_ml.utils import logger
from src.Wine_ml.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


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

