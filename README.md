# Sales_Forecasting_Platform
AI ve istatistiksel zaman serisi modellerini kullanarak ürün bazlı aylık satış tahminleri üreten uçtan uca bir satış tahmin platformu.Bu platform; veri okuma, model eğitimi, değerlendirme, tahmin üretimi ve sonuçların e-posta ile iletilmesini tek bir akışta sunar.

#🚀 Özellikler

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

# 🧠 Kullanılan Teknolojiler

Backend: Python, FastAPI

Zaman Serisi: statsmodels, Prophet

Makine Öğrenimi: XGBoost, scikit-learn

Veri İşleme: Pandas, NumPy

Frontend: HTML, CSS

Mail Servisi: SMTP

Output: Excel (xlsx)

# Katmanlar:

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

# 📊 Veri Formatı

Girdi dosyası (Kaynak_Dosya.txt) aşağıdaki kolonlara sahiptir:
URUN_KODU;TARIH;MIKTAR

# Arayüz

<img width="1870" height="887" alt="image" src="https://github.com/user-attachments/assets/88c48053-5733-4677-966c-05e06955388a" />
