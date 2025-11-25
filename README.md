
🖥️ System Inspector & Cleaner

A modern desktop app for real-time system monitoring and basic cleanup operations.
Gerçek zamanlı sistem izleme ve temel temizlik işlemleri için modern bir masaüstü uygulaması.

🎯 Overview / Genel Bakış

🇬🇧 English:
System Inspector & Cleaner monitors CPU, RAM, (and if available) GPU usage, keeps logs, and offers basic cleanup tools. It features a clean dark UI and can be packaged as a standalone executable.

🇹🇷 Türkçe:
System Inspector & Cleaner, CPU, RAM ve (varsa) GPU kullanımını izler, loglar oluşturur ve temel temizlik araçları sunar. Karanlık ve modern bir arayüze sahiptir, tek dosyalık çalıştırılabilir olarak paketlenebilir.

✅ Features / Özellikler

🇬🇧 English:

Real-time monitoring (CPU / RAM / GPU)

Logging with timestamps

Temporary file cleanup

Dark UI (customtkinter)

Buildable as .exe with PyInstaller

🇹🇷 Türkçe:

Gerçek zamanlı izleme (CPU / RAM / GPU)

Zaman damgalı log kaydı

Geçici dosya temizleme

Karanlık arayüz (customtkinter)

PyInstaller ile .exe oluşturma desteği

🖼️ Screenshots / Ekran Görüntüleri

(Add images here / Buraya ekran görüntüleri ekleyebilirsin)

📂 Project Structure / Proje Yapısı

project
├─ ui
│ └─ main.py
├─ core
│ ├─ monitor.py
│ ├─ cleaner.py
│ └─ logger.py
└─ logs

🚀 How to Run / Nasıl Çalıştırılır

🇬🇧 English:

Install Python 3.10+

Install dependencies: pip install -r requirements.txt

Run the app: python main.py

🇹🇷 Türkçe:

Python 3.10+ kurulu olmalı

Gerekli kütüphaneleri yükle: pip install -r requirements.txt

Uygulamayı başlat: python main.py

🛠️ Build .EXE / .EXE Oluşturma

PyInstaller komutu:
pyinstaller --noconsole --onefile --add-data "core;core" ui/main.py

🇬🇧 English:
The .exe file will be located in the dist/ folder.

🇹🇷 Türkçe:
Oluşan .exe dosyası dist/ klasöründe bulunur.

⚠️ Notes / Notlar

🇬🇧 English:

Cleanup operations target safe directories only.

Some actions may require admin permissions.

Logs are stored locally on the device.

🇹🇷 Türkçe:

Temizlik işlemleri yalnızca güvenli klasörlerde çalışır.

Bazı işlemler yönetici izni gerektirebilir.

Log dosyaları cihazda yerel olarak saklanır.

🚧 Future Plans / Gelecek Planları

🇬🇧 English:

Disk usage charts

Background monitoring

Temperature sensor support

Cloud log sync

🇹🇷 Türkçe:

Disk kullanım grafikleri

Arka planda izleme

Sıcaklık sensörü desteği

Bulut log senkronizasyonu

👤 Developer / Geliştirici

Erdem Aydın
