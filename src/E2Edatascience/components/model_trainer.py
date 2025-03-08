from src.E2Edatascience.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
from datetime import datetime
import joblib
import os
from src.E2Edatascience import logger

class ModelTrainer():
    def __init__(self,config:ModelTrainerConfig):
        self.config = config



    


    def train_model(self):

        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column],axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)

        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        lr.fit(train_x,train_y)
        model_name = self.config.model_name.format(algorithm_name = "ElasticNet", timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") )
        joblib.dump(lr, os.path.join(self.config.root_dir,model_name) )
        logger.info(f"Model Saved at location: {os.path.join(self.config.root_dir,model_name)} ")


        