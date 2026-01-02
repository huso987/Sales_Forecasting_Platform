# app/services/evaluation_service.py
import numpy as np

class EvaluationService:
    def mape(self, y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
