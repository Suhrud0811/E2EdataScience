from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.components.model_trainer import ModelTrainer
from src.E2Edatascience import logger



class ModelTrainingPipeline():
    def __init__(self):
        pass




    def initiate_model_trainig(self):

        manager = ConfigurationManager()
        model_trainig_config = manager.get_model_trainer_config()
        model = ModelTrainer(model_trainig_config)
        model.train_model()



STAGE_NAME = "Model Training Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        mtp = ModelTrainingPipeline()
        mtp.initiate_model_trainig()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
 


