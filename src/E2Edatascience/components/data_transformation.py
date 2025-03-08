from src.E2Edatascience import logger
from src.E2Edatascience.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd
import os


class DataTransformation():
    def __init__(self,config:DataTransformationConfig):
        self.config = config



    def initiate_train_test_split(self):

        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)

        logger.info("Splitted data into training and test sets")
        logger.info(f"Train data size: {train.shape}")
        logger.info(f"Test data size: {test.shape}")

