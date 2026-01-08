import numpy as np

class EvaluationService:
    def mape(self, y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        epsilon = 1e-5
        
        mask = np.abs(y_true) > epsilon

        if mask.sum() == 0:
            return np.inf

        mape_value = np.mean(
            np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])
        ) * 100

        return mape_value



