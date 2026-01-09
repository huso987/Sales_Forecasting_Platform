# Sales_Forecasting_Platform
AI ve istatistiksel zaman serisi modellerini kullanarak ürün bazlı aylık satış tahminleri üreten uçtan uca bir satış tahmin platformu.Bu platform; veri okuma, model eğitimi, değerlendirme, tahmin üretimi ve sonuçların e-posta ile iletilmesini tek bir akışta sunar.

## 🚀 Özellikler

🔢 Ürün Bazlı Tahminleme

📈 Çoklu Model Desteği

1-) SARIMA

2-) Holt-Winters

3-) Prophet

4-) XGBoost

⏳ Esnek Tahmin ve Holdout Süreleri

📊 Model Performans Değerlendirmesi

📤 Tahmin Sonuçlarını Excel olarak Mail Gönderimi

🧩 Modüler ve Genişletilebilir Mimari


## 📊 Veri Formatı

Girdi dosyası (Kaynak_Dosya.txt) aşağıdaki kolonlara sahiptir:
URUN_KODU;TARIH;MIKTAR


## Katmanlar:

Controller Layer:
HTTP isteklerini karşılar, doğrulama yapar ve servisleri tetikler.

Service Layer:
Tüm iş mantığı burada bulunur (veri işleme, eğitim, değerlendirme, tahmin).

Model Layer:
Tüm tahmin modelleri BaseModel üzerinden türetilmiştir.

Core Layer:
Konfigürasyon ve altyapı servislerini içerir (mail, env, path).

View Layer:
Kullanıcı arayüzü.

## Çağrı Zinciri
FastAPI Endpoint (ForecastController) 
    -> ForecastService.run()
        -> DataService.load()
        -> TrainingService.train_and_evaluate()
            -> Model.train()
            -> Model.predict()
            -> EvaluationService.mape()
        -> Mailer.send()




## UML Diyagram

![uml-diyagram](https://github.com/user-attachments/assets/e82fa018-2a5d-4adc-b58b-e5ce30fe1c56)


## Arayüz
<img width="1860" height="875" alt="image" src="https://github.com/user-attachments/assets/3f4ac5cb-2ab3-4640-bf14-8da594f9c05e" />


