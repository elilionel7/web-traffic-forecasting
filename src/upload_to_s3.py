import boto3
s3 = boto3.client('s3')
s3.upload_file("data/forecast_results.csv", "web-traffic-data-bucket", "forecast_results.csv")
print("Results uploaded successfully!")
