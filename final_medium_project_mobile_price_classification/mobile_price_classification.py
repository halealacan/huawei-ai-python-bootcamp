import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
# Veri setini oku
df = pd.read_csv("train.csv")

# İlk 5 satırı görüntüle
print("İlk 5 satır:")
print(df.head())

# Veri setinin boyutunu görüntüle
print("\nVeri setinin boyutu:")
print(df.shape)

# Sütun isimlerini görüntüle
print("\nSütunlar:")
print(df.columns)
# Eksik veri kontrolü
print("\nEksik veri sayısı:")
print(df.isnull().sum())

# Fiyat sınıflarındaki telefon sayılarını görüntüle
print("\nFiyat sınıflarının dağılımı:")
print(df["price_range"].value_counts().sort_index())
# Fiyat sınıflarının dağılımını görselleştir
fiyat_sayilari = df["price_range"].value_counts().sort_index()

plt.figure(figsize=(7, 5))
plt.bar(fiyat_sayilari.index, fiyat_sayilari.values)

plt.title("Telefon Fiyat Sınıflarının Dağılımı")
plt.xlabel("Fiyat Sınıfı")
plt.ylabel("Telefon Sayısı")
plt.xticks([0, 1, 2, 3])

plt.tight_layout()
plt.savefig("price_class_distribution.png")
plt.show()
# Fiyat sınıflarına göre ortalama RAM miktarı
ortalama_ram = df.groupby("price_range")["ram"].mean()

print("\nFiyat sınıflarına göre ortalama RAM:")
print(ortalama_ram)

plt.figure(figsize=(7, 5))
plt.bar(ortalama_ram.index, ortalama_ram.values)

plt.title("Fiyat Sınıfına Göre Ortalama RAM")
plt.xlabel("Fiyat Sınıfı")
plt.ylabel("Ortalama RAM (MB)")
plt.xticks([0, 1, 2, 3])

plt.tight_layout()
plt.savefig("average_ram_by_price_class.png")
plt.show()
# Makine öğrenmesi için özellikleri ve hedef değişkeni ayır

# X: Telefonun özellikleri
X = df.drop("price_range", axis=1)

# y: Tahmin etmek istediğimiz fiyat sınıfı
y = df["price_range"]

print("\nÖzelliklerin boyutu:")
print(X.shape)

print("\nHedef değişkenin boyutu:")
print(y.shape)
# Veriyi eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nEğitim veri sayısı:")
print(X_train.shape)

print("\nTest veri sayısı:")
print(X_test.shape)
# Random Forest modelini oluştur
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Modeli eğitim verileriyle eğit
model.fit(X_train, y_train)

print("\nModel başarıyla eğitildi.")
# Test verileri üzerinde tahmin yap
y_pred = model.predict(X_test)

# Modelin doğruluk oranını hesapla
accuracy = accuracy_score(y_test, y_pred)

print("\nModel doğruluk oranı:")
print(f"%{accuracy * 100:.2f}")
# Confusion Matrix oluştur
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Confusion Matrix'i görselleştir
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[0, 1, 2, 3]
)

disp.plot()
plt.title("Random Forest - Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.show()
# Özellik önemlerini hesapla
ozellik_onemleri = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nEn önemli 10 özellik:")
print(ozellik_onemleri.head(10))

# En önemli 10 özelliği görselleştir
ilk_10 = ozellik_onemleri.head(10)

plt.figure(figsize=(9, 6))
plt.barh(ilk_10.index[::-1], ilk_10.values[::-1])

plt.title("Fiyat Tahmininde En Önemli 10 Özellik")
plt.xlabel("Önem Düzeyi")
plt.ylabel("Telefon Özelliği")

plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()