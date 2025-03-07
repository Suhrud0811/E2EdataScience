from src.E2Edatascience.entity.config_entity import DataIngestionConfig
import urllib.request as request
import os
from src.E2Edatascience import logger
from zipfile import ZipFile


class DataIngestion():
    def __init__(self,config:DataIngestionConfig):
        self.config = config



    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"File downloaded successfully: {filename} ")


        else:
            logger.info(f"Data already exists")

    def extract_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok= True)
        with ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        

