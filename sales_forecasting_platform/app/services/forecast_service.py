import pandas as pd
from app.services.data_service import DataService
from app.core.mailer import Mailer

class ForecastService:

    def run(self, urunler, models, months, holdout, email):
        data = DataService().load()

        products = [u.strip() for u in urunler.split(",")]

        results = []

        for product in products:
            for model in models:
                for i in range(months):
                    results.append({
                        "URUN": product,
                        "MODEL": model,
                        "AY": i + 1,
                        "TAHMIN": 100
                    })

        df = pd.DataFrame(results)
        output_path = "outputs/forecasts.xlsx"
        df.to_excel(output_path, index=False)

        Mailer().send(email, output_path)
