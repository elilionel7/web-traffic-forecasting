import logging
import boto3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("pipeline.log")],
)
logger = logging.getLogger(__name__)


def upload_file_to_s3(local_file, bucket_name, s3_key):
    """Uploads a local file to an S3 bucket."""
    try:
        s3 = boto3.client("s3")
        s3.upload_file(local_file, bucket_name, s3_key)
        logger.info(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logger.error(f"Error uploading {local_file} to S3: {e}")


# Example usage
if __name__ == "__main__":
    upload_file_to_s3(
        "data/forecast_results.csv", "web-traffic-data-bucket", "forecast_results.csv"
    )
