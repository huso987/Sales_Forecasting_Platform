from statsmodels.tsa.holtwinters import ExponentialSmoothing
from app.models.base_model import BaseForecastModel

class HoltWintersModel(BaseForecastModel):
    name = "Holt-Winters"

    def train(self, series):
        self.model = ExponentialSmoothing(
            series,
            seasonal="add",
            seasonal_periods=12
        )
        self.fitted = self.model.fit()

    def predict(self, steps):
        return self.fitted.forecast(steps)
