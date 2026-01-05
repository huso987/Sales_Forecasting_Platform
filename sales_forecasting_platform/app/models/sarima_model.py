from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import ParameterGrid
from app.models.base_model import BaseForecastModel
import numpy as np

class SarimaModel(BaseForecastModel):
    name = "SARIMA"

    def train(self, series):
        self.series = series
        self.best_mape = np.inf
        self.best_model = None

        train = series

        for params in ParameterGrid({
            "p": [0, 1, 2],
            "d": [0, 1],
            "q": [0, 1, 2]
        }):
            try:
                model = SARIMAX(
                    train,
                    order=(params["p"], params["d"], params["q"]),
                    seasonal_order=(1, 1, 1, 12)
                ).fit(disp=False)

                self.best_model = model
                break
            except:
                continue

        if self.best_model is None:
            raise RuntimeError("SARIMA failed")

    def predict(self, steps):
        return self.best_model.forecast(steps)
