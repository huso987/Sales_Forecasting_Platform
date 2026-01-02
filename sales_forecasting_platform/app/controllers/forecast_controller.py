from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from app.services.forecast_service import ForecastService

class ForecastController:
    def __init__(self, templates):
        self.templates = templates
        self.service = ForecastService()

    def register(self, app):

        @app.get("/", response_class=HTMLResponse)
        async def index(request: Request):
            return self.templates.TemplateResponse(
                "index.html",
                {"request": request}
            )

        @app.post("/forecast", response_class=HTMLResponse)
        async def forecast(
            request: Request,
            urunler: str = Form(...),
            models: list[str] = Form(...),
            months: int = Form(18),
            holdout: int = Form(6),
            email: str = Form(...)
        ):
            self.service.run(
                urunler=urunler,
                models=models,
                months=months,
                holdout=holdout,
                email=email
            )

            return self.templates.TemplateResponse(
                "index.html",
                {
                    "request": request,
                    "message": "✅ Tahminler üretildi ve mail gönderildi."
                }
            )
