
import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("pipeline.log")],
)
logger = logging.getLogger(__name__)

def preprocess_data(input_file, output_file):
    """
    Preprocesses the web traffic data.
    - Converts timestamps to datetime.
    - Fills missing values.
    - Resamples data to hourly intervals.

    Args:
        input_file (str): Path to the raw data CSV file.
        output_file (str): Path to save the preprocessed CSV file.
    """
    try:
        # Load the dataset
        logger.info(f"Loading raw data from {input_file}")
        data = pd.read_csv(input_file)

        # Convert 'Timestamp' to datetime
        logger.info("Converting 'Timestamp' column to datetime")
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])

        # Check for missing values and fill them
        logger.info("Checking and filling missing values")
        data = data.set_index('Timestamp')
        data = data.resample('h').mean()  # Resample to hourly intervals
        data = data.ffill()  # Fill forward missing values

        # Save the preprocessed data
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        data.to_csv(output_file)
        logger.info(f"Preprocessed data saved to {output_file}")

    except Exception as e:
        logger.error(f"Error during preprocessing: {e}")

# Example usage
if __name__ == "__main__":
    preprocess_data("data/web_traffic.csv", "data/preprocessed_web_traffic.csv")
