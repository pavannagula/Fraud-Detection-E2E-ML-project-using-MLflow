from fraud_detection_project.constants import *
from fraud_detection_project.utils.common import read_yaml, create_directories
from fraud_detection_project.entity.config_entity import DataIngestionConfig

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
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config