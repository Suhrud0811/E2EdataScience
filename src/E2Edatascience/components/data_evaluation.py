from src.E2Edatascience.config.configuration import ConfigurationManager
from src.E2Edatascience.entity.config_entity import ModelEvaluationConfig
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.E2Edatascience import logger
import joblib
import os
import mlflow
from urllib.parse import urlparse
from src.E2Edatascience.utils.common import save_json
from pathlib import Path
from dotenv import load_dotenv,find_dotenv



class DataEvaluation():
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config



    def eval_metrics(self,actual,predictions):
        
        rmse = np.sqrt(mean_squared_error(actual,predictions))
        mae = mean_absolute_error(actual,predictions)
        r2 = r2_score(actual,predictions)

        return rmse,mae,r2
    

    def log_into_mlflow(self):


        dotenv_path = find_dotenv()
        if not dotenv_path:
            logger.warning("⚠️ .env file not found!, Please create/load all environment variables")
            
        else:
            logger.info(f"✅ .env file found: {dotenv_path}")
            load_dotenv()
   


        test_data = pd.read_csv(self.config.test_data_path)
        
        model_name_path = os.path.join(self.config.model_path,self.config.model_load_path)
        logger.info(f"model_path: {Path(model_name_path)}")
        with open(model_name_path,'r') as f:
            content = f.read()
        model_name = content.split(':')[-1]
        
        logger.info(f"Using model: {model_name}")
        model = joblib.load(os.path.join(self.config.model_path,model_name))  

        test_x = test_data.drop([self.config.target_cloumn],axis = 1)
        test_y = test_data[[self.config.target_cloumn]]


        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        mlflow.set_experiment("E2Edatascience")
        with mlflow.start_run():

            

            predicted_quality = model.predict(test_x)

            (rmse,mae,r2) = self.eval_metrics(test_y,predicted_quality)

            #Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            
            save_json(path = Path(self.config.metric_file_name),data = scores )

            logger.info("Logging experement in mlflow")
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            logger.info(f"tracking_url_type_store:{tracking_url_type_store}")
            logger.info(f"model_uri:{self.config.mlflow_uri}")


            if tracking_url_type_store != 'file':
                mlflow.sklearn.log_model(model, "model", registered_model_name = model_name)
                logger.info(f"Model successfully logged at {self.config.mlflow_uri}")
            
            else:
                mlflow.sklearn.log_model(model,"model")
                logger.info(f"Model successfully logged locally")