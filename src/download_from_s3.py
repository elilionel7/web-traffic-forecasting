import logging
import os
import boto3

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("pipeline.log"),
    ],
)
logger = logging.getLogger(__name__)


def download_file_from_s3(bucket_name, file_name, local_path):
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        s3 = boto3.client("s3")
        s3.download_file(bucket_name, file_name, local_path)
        logger.info(f"Downloaded {file_name} to {local_path}")
    except Exception as e:
        logger.error(f"Failed to download {file_name}: {e}")


if __name__ == "__main__":
    download_file_from_s3(
        "web-traffic-data-bucket", "web_traffic.csv", "data/web_traffic.csv"
    )
