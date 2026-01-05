# app/services/training_service.py

from app.models.sarima_model import SarimaModel
from app.models.hw_model import HoltWintersModel
from app.models.prophet_model import ProphetModel
from app.models.xgb_model import XGBModel
from app.services.evaluation_service import EvaluationService

MODEL_MAP = {
    "sarima": SarimaModel,
    "hw": HoltWintersModel,
    "prophet": ProphetModel,
    "xgb": XGBModel
}

class TrainingService:

    def __init__(self):
        self.evaluator = EvaluationService()

    def train_and_evaluate(self, series, selected_models, holdout):
        train = series[:-holdout]
        test = series[-holdout:]

        results = {}

        for key in selected_models:
            model = MODEL_MAP[key]()

            try:
                model.train(train)
                preds = model.predict(holdout)
                mape = self.evaluator.mape(test.values, preds)

                if mape is not None:
                    results[model.name] = {
                        "model": model,
                        "mape": float(mape)
                    }

            except Exception as e:
                continue

        return results
