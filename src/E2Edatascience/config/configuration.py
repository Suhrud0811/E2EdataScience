from src.E2Edatascience.constants import *
from src.E2Edatascience.utils.common import create_directories,read_yaml
from src.E2Edatascience.entity.config_entity import DataIngestionConfig,DataValidationConfig



class ConfigurationManager():
    def __init__(self,
              config_path = CONFIG_FILE_PATH,
              schema_path = SCHEMA_FILE_PATH,
              params_path = PARAMS_FILE_PATH
        ):
            self.config = read_yaml(config_path)
            self.params = read_yaml(params_path)
            self.schema = read_yaml(schema_path)
            
            #create base directory
            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
          
        
          config = self.config.data_ingestion
          create_directories([config.root_dir])
          data_ingestion_config = DataIngestionConfig(
                config.root_dir,
                config.source_URL,
                config.local_data_file,
                config.unzip_dir)
          
          return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
          
      config = self.config.data_validation
      schema = self.schema.COLUMNS
          
      create_directories([config.root_dir])

      data_validation_config = DataValidationConfig(
            config.root_dir,
            config.unzip_data_dir,
            config.STATUS_FILE,
            schema
      )

      return data_validation_config
    


    

               
