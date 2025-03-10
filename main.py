from src.E2Edatascience import logger
from src.E2Edatascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.E2Edatascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.E2Edatascience.pipeline.data_transformation_pipeline import DataTransformationTrainigPipeline
from src.E2Edatascience.pipeline.model_trainig_pipeline import ModelTrainingPipeline
from src.E2Edatascience.pipeline.data_evaluation_pipeline import ModelEvaluationTrainingPipeline


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