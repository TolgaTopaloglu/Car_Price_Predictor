🚀 AUTOVALUE: Uçtan Uca Araç Fiyat Tahmin ve Analiz Motoru
<img width="2542" height="1298" alt="CarPriceReg" src="https://github.com/user-attachments/assets/1a707a51-6ef5-4016-b978-ac5ed6a2171d" />
📌 Proje Hakkında

AUTOVALUE, ikinci el araçların piyasa değerini makine öğrenmesi kullanarak tahmin eden uçtan uca bir web uygulamasıdır.

Projenin temel amacı, kullanıcıdan alınan araç bilgilerini analiz ederek mümkün olduğunca doğru ve anlaşılır bir fiyat tahmini sunmaktır. Geliştirilen model, test verileri üzerinde %98.3 R² skoru elde etmiştir.

Projeyi geliştirirken özellikle veri bilimi, makine öğrenmesi ve backend tarafına odaklandım. Veri setinin hazırlanması ve temizlenmesi, EDA, veri ön işleme, model seçimi, model eğitimi ve test süreçlerini sıfırdan geliştirdim. Eğitilen modeli daha sonra FastAPI kullanarak bir API haline getirip frontend ile entegre ettim.

Frontend tarafında ise modern, sade ve Dark Mode odaklı bir kullanıcı arayüzü oluşturuldu. Arayüz tasarımı ve frontend geliştirmelerinin büyük kısmı Cursor AI tarafından gerçekleştirildi. Ben ise frontend'in backend ile entegrasyonu ve modelden dönen tahmin sonuçlarının kullanıcıya aktarılması gibi kısımları projeye uyarladım.

Bu projede benim için önemli olan nokta sadece başarılı bir makine öğrenmesi modeli oluşturmak değildi. Modeli, veri hazırlama aşamasından API geliştirmeye ve kullanıcı arayüzüne kadar gerçek hayatta kullanılabilecek bir uygulamaya dönüştürmeyi hedefledim.

🛠️ Kullanılan Teknolojiler
⚙️ Backend & API
FastAPI (0.115.12): API geliştirme ve modelin frontend ile haberleşmesi için kullanıldı.
Uvicorn (0.34.3): FastAPI uygulamasını çalıştırmak için kullanıldı.
Jinja2 (3.1.6): Dinamik HTML template'leri için kullanıldı.
Python-Multipart (0.0.20): Form verilerinin backend tarafında işlenmesi için kullanıldı.
🧠 Veri Bilimi & Makine Öğrenmesi
Scikit-Learn (1.6.1): Veri ön işleme, One-Hot Encoding, StandardScaler ve modelleme süreçlerinde kullanıldı.
XGBoost: Ana tahmin modeli olarak kullanıldı.
Pandas (2.3.0): Veri temizleme, düzenleme ve analiz süreçlerinde kullanıldı.
🎨 Frontend
HTML5 / CSS3 / JavaScript: Frontend altyapısında kullanıldı.
Cursor AI: Arayüz tasarımı ve frontend geliştirmelerinin büyük kısmında kullanıldı.
📊 Makine Öğrenmesi ve Model Performansı

Projede, veri setine en uygun modeli bulabilmek için farklı makine öğrenmesi algoritmaları test edildi ve sonuçlar R² (R-Squared) metriği üzerinden karşılaştırıldı.

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
<img width="1140" height="565" alt="CarPriceRegModel" src="https://github.com/user-attachments/assets/bb857d59-bc30-4ee3-8f33-e71eb2f944ee" />

Test sonuçlarına göre hiperparametreleri optimize edilmiş XGBoost, diğer modellere kıyasla en başarılı sonucu verdi. Bu nedenle projenin ana tahmin modeli olarak XGBoost tercih edildi.

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
<img width="367" height="431" alt="FeatureImportance" src="https://github.com/user-attachments/assets/fb4e1e9b-7c53-40e6-8afe-bcb7138b9850" />

Analiz sonucunda özellikle üretim yılı, marka ve model bilgilerinin araç fiyatı üzerinde önemli bir etkiye sahip olduğu görülmektedir.

🚀 Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları uygulayabilirsiniz.

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


Uygulama çalıştıktan sonra tarayıcınızdan aşağıdaki adrese giderek AUTOVALUE'yu kullanabilirsiniz:

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

🎯 Projenin Amacı

AUTOVALUE ile makine öğrenmesi kullanarak gerçek hayattaki bir probleme çözüm üretmeyi ve geliştirilen modeli kullanılabilir bir web uygulamasına dönüştürmeyi amaçladım.

Proje boyunca veri analizi → modelleme → API → frontend şeklinde uçtan uca bir geliştirme süreci izledim.

Bu proje sayesinde veri bilimi ve makine öğrenmesi tarafındaki çalışmalarımı, gerçek kullanıcı etkileşimi olan bir web uygulamasıyla birleştirmeyi hedefledim.
