import matplotlib.pyplot as plt


# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]


# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

print("soru 1'in çözümü")
plt.figure()
plt.plot(aylar, satislar)
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Aylık Satışlar")
plt.show()



# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.

print("soru 2'nin çözümü")
plt.figure()
plt.plot(aylar, karlar, color="red")
plt.xlabel("Aylar")
plt.ylabel("Kârlar")
plt.title("Aylık Kârlar")
plt.show()


# SORU 3
# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.

print("soru 3'ün çözümü")
plt.figure()
plt.plot(aylar, satislar, marker="o")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Aylık Satışlar (Marker'lı)")
plt.show()


# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.

print("soru 4'ün çözümü")
plt.figure()
plt.bar(aylar, satislar)
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.title("Aylık Satışlar (Bar)")
plt.show()


# SORU 5
# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.

print("soru 5'in çözümü")
plt.figure()
plt.bar(aylar, reklam, color="green")
plt.xlabel("Aylar")
plt.ylabel("Reklam")
plt.title("Aylık Reklam Harcamaları")
plt.show()


# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.

print("soru 6'nın çözümü")
plt.figure()
plt.pie(
    satislar,
    labels=aylar,
    autopct="%1.1f%%"  # yüzdeleri yazdırır
)
plt.title("Satışların Dağılımı")
plt.show()


# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.

print("soru 7'nin çözümü")
plt.figure()
plt.scatter(reklam, satislar)
plt.xlabel("Reklam")
plt.ylabel("Satışlar")
plt.title("Reklam vs Satışlar (Scatter)")
plt.show()


# SORU 8
# Reklam ve kâr verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.

print("soru 8'in çözümü")
plt.figure()
plt.scatter(reklam, karlar, color="red", s=150)  # s: nokta boyutu
plt.xlabel("Reklam")
plt.ylabel("Kârlar")
plt.title("Reklam vs Kârlar (Kırmızı Büyük Nokta)")
plt.show()


# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.
print("soru 9'un çözümü")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(aylar, satislar)
axes[0].set_xlabel("Aylar")
axes[0].set_ylabel("Satışlar")
axes[0].set_title("Satışlar (Line)")

axes[1].bar(aylar, karlar)
axes[1].set_xlabel("Aylar")
axes[1].set_ylabel("Kârlar")
axes[1].set_title("Kârlar (Bar)")

plt.tight_layout()
plt.show()



# SORU 10
# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart

print("soru 10'un çözümü")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1.grafik
axes[0, 0].plot(aylar, satislar)
axes[0, 0].set_title("Satışlar (Line)")
axes[0, 0].set_xlabel("Aylar")
axes[0, 0].set_ylabel("Satışlar")

# 2.grafik
axes[0, 1].bar(aylar, karlar)
axes[0, 1].set_title("Kârlar (Bar)")
axes[0, 1].set_xlabel("Aylar")
axes[0, 1].set_ylabel("Kârlar")

# 3.grafik
axes[1, 0].scatter(reklam, satislar)
axes[1, 0].set_title("Reklam vs Satışlar (Scatter)")
axes[1, 0].set_xlabel("Reklam")
axes[1, 0].set_ylabel("Satışlar")

# 4.grafik

axes[1, 1].pie(satislar, labels=aylar, autopct="%1.1f%%")
axes[1, 1].set_title("Satışların Dağılımı (Pie)")

plt.tight_layout()
plt.show()