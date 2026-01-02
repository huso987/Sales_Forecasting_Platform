import smtplib
from email.message import EmailMessage
from app.core.config import SMTP_HOST, SMTP_PORT, SMTP_SENDER, SMTP_PASSWORD

class Mailer:

    def send(self, to_email, attachment_path):
        msg = EmailMessage()
        msg["Subject"] = "Satış Tahmin Sonuçları"
        msg["From"] = SMTP_SENDER
        msg["To"] = to_email
        msg.set_content("Tahmin dosyanız ektedir.")

        with open(attachment_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename="forecasts.xlsx"
            )

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_SENDER, SMTP_PASSWORD)
            server.send_message(msg)
