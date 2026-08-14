import numpy as np


# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

print("soru 1'in çözümü")
dizi1 = np.arange(1, 21)
print("Dizi:", dizi1)
print("Eleman sayısı:", dizi1.size)


# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

print("soru 2'nin çözümü")
dizi2 = np.array([5, 10, 15, 20, 25])
sonuc2 = dizi2 * 3
print("Sonuç:", sonuc2)

# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

print("soru 3'ün çözümü")
dizi3 = np.arange(0, 31)
secim3 = dizi3[10:21]  # 10'dan 20'ye (slicing son dahil değil) => 10..20
print("Seçilen elemanlar (10-20):", secim3)


# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

print("soru 4'ün çözümü")
dizi4_1 = np.array([1, 2, 3])
dizi4_2 = np.array([4, 5, 6])
birlesik4 = np.concatenate((dizi4_1, dizi4_2))
print("Birleşik dizi:", birlesik4)


# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

print("soru 5'in çözümü")
dizi5 = np.arange(1, 13)
matris5 = dizi5.reshape(3, 4)
print("Matrisi:\n", matris5)
print("Shape:", matris5.shape)


# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

print("soru 6'nın çözümü")
matris6 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("Matrisin ikinci satırı:", matris6[1])
print("Matrisin ikinci sütunu:", matris6[:, 1])


# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

print("soru 7'nin çözümü")
matris7 = np.random.random((3, 3))  # 3x3 rastgele sayılar (float)
ortalama7 = matris7.mean()
maks7 = matris7.max()
print("Matris:\n", matris7)
print("Ortalama:", ortalama7)
print("Maksimum:", maks7)


# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

print("soru 8'in çözümü")
dizi8_1 = np.array([2, 4, 6, 8])
dizi8_2 = np.array([1, 3, 5, 7])
sonuc8 = dizi8_1 * dizi8_2
print("Eleman bazlı çarpım:", sonuc8)


# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

print("soru 9'un çözümü")
dizi9 = np.arange(1, 10)
matris9 = dizi9.reshape(3, 3)
transpose9 = matris9.T
print("Matris:\n", matris9)
print("Transpose:\n", transpose9)


# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

print("soru 10'un çözümü")
dizi10 = np.random.randint(1, 51, size=10)  # 1 ile 50 arası, 10 tam sayı
toplam10 = dizi10.sum()
ortalama10 = dizi10.mean()
print("Dizi:", dizi10)
print("Toplam:", toplam10)
print("Ortalama:", ortalama10)