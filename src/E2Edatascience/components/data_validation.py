from src.E2Edatascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation():
    def __init__(self,config:DataValidationConfig):
        self.config = config


    def initiate_validation(self) -> bool:

        try:
            validation_status = False

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_dtypes = list(map(str, data.dtypes))
        
            all_schema_columns = list(self.config.all_schema.keys())
            all_schema_values = list(self.config.all_schema.values())

            for i in range(len(all_cols)):
                if ((all_cols[i] == all_schema_columns[i]) and (all_dtypes[i] == all_schema_values[i])):

                # if col not in all_schema_columns:
                    validation_status = True
                else:
                    validation_status = False
                    break

            with open(self.config.STATUS_FILE,'w') as file:
                        file.write(f"Validation Status: {validation_status}")

            return validation_status
        
        except Exception as e:
             raise e