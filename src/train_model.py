import logging
import pandas as pd
from prophet import Prophet
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("pipeline.log")],
)
logger = logging.getLogger(__name__)

def train_and_save_forecast(data_path, output_path, forecast_days=30):
    """Trains a Prophet model on the dataset and saves the forecast."""
    try:
        logger.info(f"Loading data from {data_path}")
        data = pd.read_csv(data_path)
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data.rename(columns={"Timestamp": "ds", "TrafficCount": "y"}, inplace=True)

        logger.info("Training Prophet model")
        model = Prophet()
        model.fit(data)

        logger.info(f"Generating forecast for the next {forecast_days} days")
        future = model.make_future_dataframe(periods=forecast_days)
        forecast = model.predict(future)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(output_path, index=False)
        logger.info(f"Forecast results saved to {output_path}")

    except Exception as e:
        logger.error(f"Error training model or saving forecast: {e}")

if __name__ == "__main__":
    train_and_save_forecast("data/web_traffic.csv", "data/forecast_results.csv")
