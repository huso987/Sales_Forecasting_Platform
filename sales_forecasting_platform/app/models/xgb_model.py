import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from app.models.base_model import BaseForecastModel

class XGBModel(BaseForecastModel):
    name = "XGBOOST"

    def train(self, series: pd.Series):
        self.lags = 12

        values = series.values.astype(float)

        if len(values) <= self.lags:
            raise ValueError("XGBoost için veri yetersiz")

        df = pd.DataFrame({"y": values})

        # Lag features
        for i in range(1, self.lags + 1):
            df[f"lag_{i}"] = df["y"].shift(i)

        df = df.dropna()

        X = df.drop("y", axis=1)
        y = df["y"]

        self.model = XGBRegressor(
            n_estimators=400,
            max_depth=5,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="reg:squarederror",
            random_state=42
        )

        self.model.fit(X, y)

        # History for recursive prediction
        self.history = values.tolist()

    def predict(self, steps: int):
        preds = []

        for _ in range(steps):
            last_lags = self.history[-self.lags:]

            X_input = pd.DataFrame(
                [last_lags[::-1]],
                columns=[f"lag_{i}" for i in range(1, self.lags + 1)]
            )

            yhat = float(self.model.predict(X_input)[0])

            preds.append(yhat)
            self.history.append(yhat)

        return preds
