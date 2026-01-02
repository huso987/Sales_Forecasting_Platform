# app/models/xgb_model.py
import numpy as np
from xgboost import XGBRegressor
from app.models.base_model import BaseForecastModel

class XGBModel(BaseForecastModel):
    name = "XGBoost"
    def train(self, series):
        X, y = [], []
        for i in range(12, len(series)):
            X.append(series.values[i-12:i])
            y.append(series.values[i])
        self.model = XGBRegressor()
        self.model.fit(X, y)
        self.last_window = series.values[-12:]

    def predict(self, steps):
        preds = []
        window = self.last_window
        for _ in range(steps):
            p = self.model.predict([window])[0]
            preds.append(p)
            window = list(window[1:]) + [p]
        return preds
