#!/bin/bash
echo "Starting pipeline..." | tee -a pipeline.log

# Step 1: Download the dataset
python src/download_from_s3.py | tee -a pipeline.log

# Step 2: Preprocess dataset
python src/preprocess.py | tee -a pipeline.log

# Step 3: Train the model and generate forecast
python src/train_model.py | tee -a pipeline.log

# Step 3: Upload the forecast results
python src/upload_to_s3.py | tee -a pipeline.log

echo "Pipeline completed successfully!" | tee -a pipeline.log
