import boto3
bucket_name = "web-traffic-data-bucket"
s3_key = "web_traffic.csv"
local_file = "data/web_traffic.csv"
s3 = boto3.client('s3')
s3.download_file(bucket_name, s3_key, local_file)
print("File downloaded successfully!")
