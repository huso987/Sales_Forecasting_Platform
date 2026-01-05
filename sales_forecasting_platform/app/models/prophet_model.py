from prophet import Prophet
import pandas as pd
from app.models.base_model import BaseForecastModel

class ProphetModel(BaseForecastModel):
    name = "Prophet"

    def train(self, series: pd.Series):
        # Index -> ds, values -> y
        df = series.reset_index()
        df.columns = ["ds", "y"]

        # ZORLA FORMAT VERME → Prophet kendi çözer
        df["ds"] = pd.to_datetime(df["ds"], errors="coerce")
        df["y"] = pd.to_numeric(df["y"], errors="coerce")

        df = df.dropna()

        if len(df) < 12:
            raise ValueError("Prophet için en az 12 gözlem gerekli")

        # Frequency otomatik tespit
        self.freq = pd.infer_freq(df["ds"])
        if self.freq is None:
            self.freq = "M"

        self.model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=False,
            daily_seasonality=False
        )

        self.model.fit(df)

        self.train_len = len(df)

    def predict(self, steps: int):
        future = self.model.make_future_dataframe(
            periods=steps,
            freq=self.freq
        )

        forecast = self.model.predict(future)

        # EN KRİTİK SATIR 👇
        return forecast["yhat"].iloc[-steps:].values
