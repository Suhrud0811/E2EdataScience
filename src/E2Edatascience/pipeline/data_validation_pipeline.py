
from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.components.data_validation import DataValidation
from src.E2Edatascience import logger

STAGE_NAME = "Training Data Validation"



class DataValidationTrainingPipeline():
    def __init__(self):
        pass



    def validate_data(self):
        
        manager = ConfigurationManager()
        validation_config = manager.get_data_validation_config()
        component = DataValidation(validation_config)
        component.initiate_validation()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        dvtp = DataValidationTrainingPipeline()
        dvtp.validate_data()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e