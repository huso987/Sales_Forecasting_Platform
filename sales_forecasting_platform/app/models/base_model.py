class BaseForecastModel:
    name = "base"

    def train(self, series):
        pass

    def predict(self, months: int):
        return [0] * months
