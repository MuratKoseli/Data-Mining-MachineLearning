# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:47:24 2024

@author: Kosel
"""

# Gerekli kütüphaneleri yükleyin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Excel dosyasından verileri okuyun
excel_path = 'veri.xlsx'  # Excel dosyasının yolunu belirtin
veri = pd.read_excel(excel_path)

# Bağımsız değişkenleri ve hedef değişkeni seçin
X = veri[['Kadro Derinliği', 'Yaş Ortalaması', 'Lejyonerler', 'Oyuncuların Piyasa Değeri Ortalaması', 'Takım Piyasa Değeri', 'Stadyum Kapasitesi']]
y = veri['Başarı']  # 'basari' hedef değişkenin adı, evet/hayır olarak etiketlenmiş olmalıdır

# 'evet' ve 'hayır' etiketlerini 0 ve 1'e dönüştürün
y = y.map({'Hayır': 0, 'Evet': 1})

# Özellikleri Min-Max ölçeklendirmesi ile 0-1 aralığına getirin
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Eğitim ve test veri setlerini oluşturun
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=98)

# KNN modelini oluşturun ve eğitin
knn_model = KNeighborsClassifier(n_neighbors=2)  # n_neighbors, komşu sayısını belirten bir parametredir
knn_model.fit(X_train, y_train)

# Test veri seti üzerinde tahmin yapın
y_pred = knn_model.predict(X_test)

# Modelin başarısını değerlendirin
accuracy = accuracy_score(y_test, y_pred)
print(f'Modelin doğruluk oranı: {accuracy}')

# İsterseniz modeli kullanarak yeni veriler üzerinde tahmin yapabilirsiniz
# yeni_veri = pd.DataFrame({'Kadro Derinliği': ..., 'Yaş Ortalaması': ..., 'Lejyonerler': ..., 'Oyuncuların Piyasa Değeri Ortalaması': ..., 'Takım Piyasa Değeri': ..., 'Stadyum Kapasitesi': ...}, index=[0])
# yeni_veri_scaled = scaler.transform(yeni_veri)
# tahmin = knn_model.predict(yeni_veri_scaled)
# print(f'Tahmin: {tahmin}')
y_pred = knn_model.predict(X_test)
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
