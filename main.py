from fraud_detection_project import logger
from fraud_detection_project.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline

STAGE_01 = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_01} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_01} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e