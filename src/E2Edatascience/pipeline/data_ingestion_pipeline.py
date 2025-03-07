from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.components.data_ingestion import DataIngestion
from src.E2Edatascience import logger


STAGE_NAME = "Traning Data Ingestion"



class DataIngestionTrainingPipeline():
    def __init__(self):
        pass



    def initiate_data_ingestion(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_file()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        ditp = DataIngestionTrainingPipeline()
        ditp.initiate_data_ingestion()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
