from prophet import Prophet
def train_and_forecast(data, periods=720):
    data = data.reset_index().rename(columns={"Timestamp": "ds", "TrafficCount": "y"})
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=periods, freq='H')
    forecast = model.predict(future)
    return forecast
