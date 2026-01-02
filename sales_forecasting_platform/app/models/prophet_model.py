# app/models/prophet_model.py
from prophet import Prophet
import pandas as pd
from app.models.base_model import BaseForecastModel

class ProphetModel(BaseForecastModel):
    name = "Prophet"
    def train(self, series):
        df = series.reset_index()
        df.columns = ["ds", "y"]
        self.model = Prophet()
        self.model.fit(df)

    def predict(self, steps):
        future = self.model.make_future_dataframe(periods=steps, freq="MS")
        forecast = self.model.predict(future)
        return forecast["yhat"].tail(steps).values
