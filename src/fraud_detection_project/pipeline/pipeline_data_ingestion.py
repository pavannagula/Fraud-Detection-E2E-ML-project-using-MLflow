from fraud_detection_project.config.configuration import *
from fraud_detection_project.components.Data_Ingestion import DataIngestion
from fraud_detection_project import logger


STAGE_01 = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()


    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_01} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_01} completed <<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e