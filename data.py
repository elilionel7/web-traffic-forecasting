import kaggle

kaggle.api.dataset_download_files(
    "raminhuseyn/web-traffic-time-series-dataset",
    path="data",
    unzip=True
)

print("Dataset downloaded and extracted to the 'data' folder.")
