🚀 AUTOVALUE: Uçtan Uca Araç Fiyat Tahmin ve Analiz Motoru
<img width="850" alt="AUTOVALUE Uygulama Ekranı" src="https://github.com/user-attachments/assets/7da9aa11-089f-4532-a84e-b4187ed79595" />
📌 Proje Hakkında

AUTOVALUE, ikinci el araçların piyasa değerini makine öğrenmesi kullanarak tahmin eden uçtan uca bir web uygulamasıdır.

Projenin temel amacı, kullanıcıdan alınan araç bilgilerini analiz ederek mümkün olduğunca doğru ve anlaşılır bir fiyat tahmini sunmaktır. Geliştirdiğim model, test verileri üzerinde %98.3 R² skoru elde etmiştir.

Projeyi geliştirirken özellikle veri bilimi, makine öğrenmesi ve backend tarafına odaklandım. Veri setinin hazırlanması ve temizlenmesi, Keşifçi Veri Analizi (EDA), veri ön işleme, model seçimi, model eğitimi ve test süreçlerini sıfırdan geliştirdim. Daha sonra eğitilen modeli FastAPI kullanarak bir API haline getirip frontend ile entegre ettim.

Frontend tarafında ise modern, sade ve Dark Mode odaklı bir kullanıcı arayüzü oluşturuldu. Arayüz tasarımı ve frontend geliştirmelerinin büyük kısmı Cursor AI tarafından gerçekleştirildi. Backend ve makine öğrenmesi tarafının frontend ile entegrasyonunu ise projeye kendim uyarladım.

Bu projede benim için önemli olan nokta sadece başarılı bir makine öğrenmesi modeli oluşturmak değildi. Veri hazırlama aşamasından modellemeye, API geliştirmeden kullanıcı arayüzüne kadar tüm süreci bir bütün olarak ele alarak, modeli gerçek hayatta kullanılabilecek bir web uygulamasına dönüştürmeyi hedefledim.

🛠️ Mimari ve Kullanılan Teknolojiler
⚙️ Backend & API
FastAPI (0.115.12): Modeli frontend'e bağlamak ve API altyapısını oluşturmak için kullanıldı.
Uvicorn (0.34.3): FastAPI uygulamasını çalıştırmak için kullanıldı.
Jinja2 (3.1.6): Dinamik HTML template'leri için kullanıldı.
Python-Multipart (0.0.20): Form verilerinin backend tarafında işlenmesi için kullanıldı.
🧠 Veri Bilimi & Makine Öğrenmesi
Scikit-Learn (1.7.0): Veri ön işleme, One-Hot Encoding, StandardScaler ve modelleme süreçlerinde kullanıldı.
XGBoost: Projenin ana tahmin modeli olarak kullanıldı.
Pandas (2.3.0): Veri temizleme, düzenleme ve analiz süreçlerinde kullanıldı.
🎨 Frontend
HTML5 / CSS3 / JavaScript: Frontend altyapısında kullanıldı.
Cursor AI: Frontend arayüz tasarımı ve geliştirmelerinin büyük kısmında kullanıldı.
📊 Makine Öğrenmesi ve Model Performansı

Projede veri setine en uygun modeli bulabilmek için farklı makine öğrenmesi algoritmaları test edildi ve sonuçlar R² (R-Squared) metriği üzerinden karşılaştırıldı.

🏆 Model Karşılaştırması
Model	R² Skoru
🥇 XGB ParamTuning	%98.3 (0.983)
🥈 XGBoost	%98.0 (0.980)
🥉 LightGBM	%97.9 (0.979)
Polynomial Regression	%97.6 (0.976)
Random Forest	%96.9 (0.969)
Gradient Boosting	%95.7 (0.957)
Decision Tree	%93.9 (0.939)
KNN	%85.5 (0.855)
Linear / Lasso / Ridge Regression	%84.4 (0.844)
AdaBoost	%74.2 (0.742)
ElasticNet	%67.1 (0.671)
SVR	-%9.1 (-0.091)
<img width="900" alt="Model Performans Karşılaştırması" src="https://github.com/user-attachments/assets/bb857d59-bc30-4ee3-8f33-e71eb2f944ee" />

Test sonuçlarına göre hiperparametreleri optimize edilmiş XGBoost, diğer modeller arasında en başarılı sonucu verdi. Bu nedenle sistemin ana tahmin modeli olarak XGBoost tercih edildi.

🔍 Özellik Önemi (Feature Importance)

Modelin araç fiyatını tahmin ederken hangi özelliklerden daha fazla etkilendiğini görmek için feature importance analizi yapıldı.

Öne çıkan özellikler:

Üretim Yılı (num__Year) — 0.1083
Marka: BMW (cat__Make_BMW) — 0.1011
Marka: Mercedes-Benz (cat__Make_Mercedes-Benz) — 0.0935
Kasa Tipi: Sedan (cat__Body_Type_Sedan) — 0.0674
Model: Audi Q7 (cat__Model_Q7) — 0.0649
Model: Audi A6 (cat__Model_A6) — 0.0611
Kasa Tipi: SUV (cat__Body_Type_SUV) — 0.0370
<img width="550" alt="Feature Importance" src="https://github.com/user-attachments/assets/fb4e1e9b-7c53-40e6-8afe-bcb7138b9850" />

Analiz sonucunda özellikle üretim yılı, marka ve model bilgilerinin araç fiyatı üzerinde önemli bir etkiye sahip olduğu görülmektedir.

💻 Uygulama Özellikleri
Etkileşimli Arayüz: Marka, model, yıl, vites, yakıt tipi, kasa tipi ve diğer araç özellikleri kolayca seçilebilir.
Anlık Fiyat Tahmini: Form gönderildiğinde araç bilgileri backend'e gönderilir, model tarafından işlenir ve tahmini fiyat kullanıcıya gösterilir.
Veri Doğrulama: Girilen araç bilgilerinin belirlenen sınırlar içerisinde ve birbiriyle uyumlu olması kontrol edilir.
Responsive Tasarım: Uygulama farklı ekran boyutlarına uyum sağlayacak şekilde tasarlanmıştır.
Dark Mode: Modern ve sade bir kullanıcı deneyimi için karanlık tema kullanılmıştır.
🖥️ Uygulama Akışı

Kullanıcı araç bilgilerini girdikten sonra veriler FastAPI backend'ine gönderilir. Backend tarafında gerekli veri ön işleme adımları uygulanır ve hazırlanan veri XGBoost modeline aktarılır.

Modelin ürettiği tahmin sonucu tekrar frontend'e gönderilir ve kullanıcıya tahmini piyasa fiyatı olarak gösterilir.

Kullanıcı
   ↓
Araç Bilgileri
   ↓
Frontend
   ↓
FastAPI API
   ↓
Data Preprocessing
   ↓
XGBoost Model
   ↓
Fiyat Tahmini
   ↓
Frontend
   ↓
Kullanıcı

🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Projeyi Klonlayın
git clone https://github.com/KULLANICI_ADINIZ/arac-fiyat-tahmin.git
cd arac-fiyat-tahmin

2. Sanal Ortam Oluşturun

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3. Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt

4. Uygulamayı Çalıştırın
uvicorn main:app --reload


Ardından tarayıcıdan aşağıdaki adrese giderek uygulamayı açabilirsiniz:

http://127.0.0.1:8000

📁 Proje Yapısı
AUTOVALUE/
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── model.pkl
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── main.py
├── requirements.txt
└── README.md


Proje yapısı, mevcut klasör ve dosya isimlerine göre güncellenebilir.

🎯 Projenin Amacı

AUTOVALUE ile makine öğrenmesi kullanarak gerçek hayattaki bir probleme çözüm üretmeyi ve geliştirilen modeli kullanılabilir bir web uygulamasına dönüştürmeyi amaçladım.

Proje boyunca veri analizi → veri ön işleme → modelleme → API → frontend şeklinde uçtan uca bir geliştirme süreci izledim.

Bu proje sayesinde makine öğrenmesi tarafındaki çalışmalarımı gerçek bir kullanıcı deneyimiyle birleştirerek, sadece bir model değil uçtan uca çalışan bir uygulama geliştirmeyi hedefledim.
