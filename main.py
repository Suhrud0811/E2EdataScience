from src.E2Edatascience import logger
from src.E2Edatascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline



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

