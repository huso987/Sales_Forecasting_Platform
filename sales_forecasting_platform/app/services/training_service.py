from app.models.sarima_model import SarimaModel
from app.models.hw_model import HoltWintersModel
from app.models.prophet_model import ProphetModel
from app.models.xgb_model import XGBModel
from app.services.evaluation_service import EvaluationService

class TrainingService:

    def __init__(self):
        self.models = [
            SarimaModel(),
            HoltWintersModel(),
            ProphetModel(),
            XGBModel()
        ]
        self.evaluator = EvaluationService()

    def train_and_select(self, series, holdout):
        train = series[:-holdout]
        test = series[-holdout:]

        results = []

        for model in self.models:
            try:
                model.train(train)
                preds = model.predict(holdout)
                score = self.evaluator.mape(test.values, preds)
                results.append((score, model))
            except Exception:
                continue

        results.sort(key=lambda x: x[0])
        return results[0][1]
