from src.E2Edatascience.entity.config_entity import DataTransformationConfig
from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.components.data_transformation import DataTransformation
from src.E2Edatascience import logger

class DataTransformationTrainigPipeline():
    def __init__(self):
        pass




    def start_data_transformation(self):
        try:

            manager = ConfigurationManager()
            data_transformation_config = manager.get_data_transformation_config()

            with open(data_transformation_config.STATUS_FILE,'r') as f:   
                validation_status = f.read().split(" ")[-1]

                if bool(validation_status): 
            
                    data_transformation = DataTransformation(data_transformation_config)
                    data_transformation.initiate_train_test_split()
                else:
                    logger.info("Dataset not validated, please validate data.")


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