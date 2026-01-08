import pandas as pd
import numpy as np

class DataService:

    def load(self, path="data/Kaynak_Dosya.txt"):
        df = pd.read_csv(path, sep=";")

        df["TARIH"] = pd.to_datetime(df["TARIH"])
        df = df.sort_values(["URUN_KODU", "TARIH"])

        return df

    def prepare_series(self, df, urun_kodu):
        ts = (
            df[df["URUN_KODU"] == urun_kodu]
            .set_index("TARIH")[["MIKTAR"]]
            .asfreq("MS")
        )

     
        ts["MIKTAR"] = ts["MIKTAR"].interpolate(method="linear")

        return ts["MIKTAR"]


    def remove_outliers(self, series, window=6):
        rolling_med = series.rolling(window, center=True).median()
        diff = (series - rolling_med).abs()

        threshold = 3 * diff.median()

        cleaned = series.where(diff <= threshold, rolling_med)

        return cleaned

    def make_stationary(self, series):
        from app.services.time_series_tests import TimeSeriesTestService

        tester = TimeSeriesTestService()
        adf_result = tester.adf_test(series)

        if not adf_result["is_stationary"]:
            return series.diff().dropna(), True

        return series, False


