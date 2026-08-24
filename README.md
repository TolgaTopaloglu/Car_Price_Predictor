# 🚀 AUTOVALUE: Uçtan Uca Araç Fiyat Tahmin ve Analiz Motoru (End-to-End Car Price Predictor)

<img width="2542" height="1298" alt="CarPriceReg" src="https://github.com/user-attachments/assets/1a707a51-6ef5-4016-b978-ac5ed6a2171d" />

## 📌 Proje Hakkında

**AUTOVALUE**, ikinci el araçların güncel piyasa değerini makine öğrenmesi algoritmalarıyla tahmin eden uçtan uca bir web uygulamasıdır. Temel amacım, kullanıcıdan alınan araç özelliklerini analiz ederek en doğru ve anlaşılır fiyat tahminini sunmaktır. Geliştirdiğim model, test verileri üzerinde **%98.3 R² skoru** elde ederek yüksek bir başarı oranı yakalamıştır.

Geliştirme sürecinde odağımı ağırlıklı olarak veri bilimi ve arka uç (backend) mimarisine verdim. Veri setinin hazırlanıp temizlenmesi, Keşifçi Veri Analizi (EDA), veri ön işleme, model seçimi, eğitimi ve test aşamalarının tamamını sıfırdan kurguladım. Ardından, eğittiğim bu modeli **FastAPI** kullanarak yüksek performanslı bir API haline getirdim.

Kullanıcı arayüzünde (Frontend) ise modern, sade ve "Dark Mode" odaklı rahat bir deneyim sunmayı hedefledim. Emeğimi daha çok veri ve modelleme tarafına ayırabilmek adına, ön yüz tasarımı ve bazı entegrasyon aşamalarında **Cursor AI** asistanından destek aldım.

Benim için bu projenin en değerli yanı, sadece arka planda çalışan bir makine öğrenmesi modeli geliştirmekle kalmayıp; veri hazırlığından API yazımına, modellemeden son kullanıcı arayüzüne kadar uzanan tüm süreci bir bütün olarak ele almaktı. Sonuç olarak, yapay zeka destekli bir modeli **gerçek hayatta kullanılabilecek, tam kapsamlı bir ürüne (end-to-end application)** dönüştürmeyi başardım.

---

## 🛠️ Mimari ve Kullanılan Teknolojiler (Tech Stack)

Proje, modern ve yüksek performanslı kütüphaneler kullanılarak inşa edilmiştir. Uygulamanın bel kemiğini oluşturan teknoloji yığını ve sürümleri şu şekildedir:

### ⚙️ Backend & API
* **[FastAPI](https://fastapi.tiangolo.com/) (`fastapi==0.115.12`):** Modern, hızlı ve asenkron API altyapısı için kullanıldı. 
* **Uvicorn (`uvicorn==0.34.3`):** Uygulamayı sunmak için ASGI sunucusu olarak tercih edildi.
* **Jinja2 (`Jinja2==3.1.6`):** HTML şablonlarını (template) sunucu tarafında işlemek ve dinamik verileri frontend'e aktarmak için kullanıldı.
* **Python-Multipart (`python-multipart==0.0.20`):** Kullanıcıdan gelen form verilerinin ayrıştırılması ve API'ye güvenli şekilde aktarılması sağlandı.

### 🧠 Veri Bilimi & Makine Öğrenmesi (Machine Learning Core)
* **[Scikit-Learn](https://scikit-learn.org/) (`scikit-learn==1.6.1`):** Veri ön işleme (One-Hot Encoding, StandardScaler) ve temel makine öğrenmesi modellerinin kurulması.
* **[XGBoost](https://xgboost.readthedocs.io/) (`xgboost`):** Projenin en başarılı ve ana tahmin modeli olarak kullanıldı. Extreme Gradient Boosting algoritması ile yüksek performans elde edildi.
* **[Pandas](https://pandas.pydata.org/) (`pandas==2.3.0`):** Veri setinin okunması, temizlenmesi, manipülasyonu ve modele hazır hale getirilmesi süreçlerinde kullanıldı.

### 🎨 Frontend
* **HTML5 / CSS3 / JavaScript:** Duyarlı (Responsive) tasarım, dinamik form yönetimi ve asenkron API istekleri (Fetch API).

---

## 📊 Makine Öğrenmesi Modelleri ve Performans Analizi (Model Performance)

Proje geliştirilirken verisetine uygun en iyi modeli bulmak amacıyla birçok farklı algoritma denenmiş ve `R² (R-Squared)` metriklerine göre karşılaştırılmıştır. 

### 🏆 Karşılaştırmalı Model Skorları (R² Score)
Analiz sonuçlarına göre test edilen modeller ve başarı oranları:

* **XGB ParamTuning (Hiperparametre Optimizasyonlu): %98.3 (0.983) 🥇 (Seçilen Model)**
* **XGBoost (Varsayılan):** %98.0 (0.980) 🥈
* **LightGBM:** %97.9 (0.979) 🥉
* **Polynomial Regression:** %97.6 (0.976)
* **Random Forest:** %96.9 (0.969)
* **Gradient Boosting:** %95.7 (0.957)
* **Decision Tree:** %93.9 (0.939)
* **KNN:** %85.5 (0.855)
* **Linear / Lasso / Ridge Regression:** %84.4 (0.844)
* **AdaBoost:** %74.2 (0.742)
* **ElasticNet:** %67.1 (0.671)
* **SVR:** -%9.1 (-0.091) *(Verisetine uygun bulunmadı)*

  <img width="1140" height="565" alt="CarPriceRegmModel" src="https://github.com/user-attachments/assets/bb857d59-bc30-4ee3-8f33-e71eb2f944ee" />

*Sonuç:* Ağaç tabanlı (Tree-based) ve Gradient Boosting modelleri kategorik ve sayısal özellikleri harmanlamada en yüksek performansı göstermiştir. Bu doğrultuda sistemin çekirdeğine hiperparametreleri optimize edilmiş **XGBoost** entegre edilmiştir.

### 🔍 Özellik Önemi (Feature Importance)
Modelin bir aracın fiyatını belirlerken en çok hangi özelliklere dikkat ettiği analiz edilmiştir:
1. **Üretim Yılı (`num__Year`):** `0.1083` - Aracın model yılı, fiyat üzerindeki en belirleyici etken.
2. **Marka: BMW (`cat__Make_BMW`):** `0.1011`
3. **Marka: Mercedes-Benz (`cat__Make_Mercedes-Benz`):** `0.0935`
4. **Kasa Tipi: Sedan (`cat__Body_Type_Sedan`):** `0.0674`
5. **Model: Audi Q7 (`cat__Model_Q7`):** `0.0649`
6. **Model: Audi A6 (`cat__Model_A6`):** `0.0611`
7. **Kasa Tipi: SUV (`cat__Body_Type_SUV`):** `0.0370`

<img width="367" height="431" alt="Featureİmportance" src="https://github.com/user-attachments/assets/fb4e1e9b-7c53-40e6-8afe-bcb7138b9850" />

Bu veriler, lüks segment araçların marka ve model verilerinin, standart özelliklerin ötesinde fiyatta büyük çarpan etkisi yarattığını doğrulamaktadır.

---

## 🚀 Kurulum ve Çalıştırma (Installation)

Projeyi kendi lokal ortamınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayın.

### 1. Projeyi Klonlayın
```bash
git clone [https://github.com/KULLANICI_ADINIZ/arac-fiyat-tahmin.git](https://github.com/KULLANICI_ADINIZ/arac-fiyat-tahmin.git)
cd arac-fiyat-tahmin




<img width="367" height="431" alt="Featureİmportance" src="https://github.com/user-attachments/assets/fb4e1e9b-7c53-40e6-8afe-bcb7138b9850" />


