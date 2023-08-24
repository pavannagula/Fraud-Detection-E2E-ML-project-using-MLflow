from fraud_detection_project.constants import *
from fraud_detection_project.utils.common import read_yaml, create_directories
from fraud_detection_project.entity.config_entity import (DataIngestionConfig, 
                                                         DataValidationConfig)

class ConfigurationManager:
    # First setting up the environment by defining the file paths of configuration file, params file and schema file.  
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        # Creating the root directory in the artifacts folder
        create_directories([self.config.artifacts_root])


    # Data Ingestion step
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            # We are accessing the file paths that are defined in the configuration yaml file
            root_dir=config.root_dir,
            s3_bucket=config.s3_bucket,
            s3_object_key=config.s3_object_key,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            data_dir = config.data_dir,
            all_schema=schema,
        )

        return data_validation_config