# app/models/sarima_model.py
from statsmodels.tsa.statespace.sarimax import SARIMAX
from app.models.base_model import BaseForecastModel

class SarimaModel(BaseForecastModel):
    name = "SARIMA"
    def train(self, series):
        self.model = SARIMAX(series, order=(1,1,1), seasonal_order=(1,1,1,12))
        self.fit = self.model.fit(disp=False)

    def predict(self, steps):
        return self.fit.forecast(steps)
