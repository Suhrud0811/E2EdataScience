from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.components.data_evaluation import DataEvaluation
from src.E2Edatascience import logger







class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass



    def initiate_evaluation(self):

        manager = ConfigurationManager()
        evaluation_config = manager.get_model_evaluation_config()
        evaluation = DataEvaluation(evaluation_config)
        evaluation.log_into_mlflow()


STAGE_NAME = "Data Evaluation"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        detp = ModelEvaluationTrainingPipeline()
        detp.initiate_evaluation()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e