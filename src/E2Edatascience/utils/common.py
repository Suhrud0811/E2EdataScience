import os
import sys
from box import ConfigBox
from ensure import ensure_annotations
from src.E2Edatascience import logger
import json
import joblib
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
import yaml

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    '''
        Reads yaml file and returns

        Args:
            path_to_yaml (str): path to input

        Raises: 
            ValueError: if yaml file is empty
            e: empty file

        Returns:
            ConfigBox: ConfigBox type
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded Successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.error(f"yaml file: {path_to_yaml} is empty")
        raise ValueError("Yaml file empty")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True) 
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose= True):
    '''
        Creates directories

        Args: 
        path_to_directories (list): list of path to directories
        verbose(bool): ignore if multiple directories are to be created,Defaults to true
    '''
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    '''
        Saves the json file to specified path

        Args:
        path (Path): path to save Json file
        data(dict): data to be saved in Json file
    '''
    with open(path,'w') as file:
        json.dump(data,file,indent=4)

    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    '''
        Loads and returns the json file

        Args:
        path(Path): Path of the json file

        returns:
            data as class attribute instead of dict
    '''

    with open(path,'r') as f:
        content = json.load(f)

    logger.info(f"Json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(path:Path, data:Any):
    '''
        Saves the data to the specified path
        Args:
        path(Path): Path of the json file
        data(Any): data in any format

    '''
    joblib.dump(value=data,path=path)
    logger.info(f"File saved to path: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    '''
        Loads the data from the specified path
        Args:
            path(Path): Path of the json file

        returns:
            data(Any): data in any format

    '''
    data = joblib.load(path=path)
    logger.info(f"File loaded from path: {path}")
    return data