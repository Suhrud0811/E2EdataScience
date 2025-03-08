from src.E2Edatascience import logger
from src.E2Edatascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.E2Edatascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.E2Edatascience.pipeline.data_transformation_pipeline import DataTransformationTrainigPipeline



STAGE_NAME = "Traning Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        ditp = DataIngestionTrainingPipeline()
        ditp.initiate_data_ingestion()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training Data Validation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        dvtp = DataValidationTrainingPipeline()
        dvtp.validate_data()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Data Transformation Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        dttp = DataTransformationTrainigPipeline()
        dttp.start_data_transformation()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e