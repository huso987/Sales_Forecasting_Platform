from statsmodels.tsa.holtwinters import ExponentialSmoothing
from app.models.base_model import BaseForecastModel

class HoltWintersModel(BaseForecastModel):
    name = "HOLT_WINTERS"

    def train(self, series):
        self.series = series

        if len(series) >= 24:
            self.model = ExponentialSmoothing(
                series,
                trend="add",
                seasonal="add",
                seasonal_periods=12
            ).fit()
        else:
            self.model = ExponentialSmoothing(
                series,
                trend="add",
                seasonal=None
            ).fit()

    def predict(self, steps):
        return self.model.forecast(steps)
