import src
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import  CustomException

load_dotenv()

logger=get_logger(__name__)

#main

def main():
    try:
        logger.info("Starting to build pipeline")
        loader=AnimeDataLoader(r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\LLMOps\ANIME_RECOMMENDER\data\anime_with_synopsis.csv",r"C:\Users\Dhivya\OneDrive - CONVERSE Data Solutions\LLMOps\ANIME_RECOMMENDER\data\anime_updated.csv") # type: ignore
        processed_csv=loader.load_and_process()
        logger.info("Data loade and processed")


        vector_builder=VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vectorstore Built successfully")
        logger.info("pipeline built successfully")


    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("error during pipeline running",e)


if __name__=="__main__":
    main()
