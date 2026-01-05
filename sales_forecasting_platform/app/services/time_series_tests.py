from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf

class TimeSeriesTestService:

    def adf_test(self, series):
        result = adfuller(series.dropna())
        return {
            "adf_stat": result[0],
            "p_value": result[1],
            "is_stationary": result[1] < 0.05
        }

    def acf_pacf(self, series, lags=24):
        return {
            "acf": acf(series.dropna(), nlags=lags),
            "pacf": pacf(series.dropna(), nlags=lags)
        }
