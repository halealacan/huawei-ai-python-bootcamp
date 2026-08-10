#soru 1
ad ="hale"
yas = 22
ortalama = 2.80
print(type(ad))
print(type(yas))
print(type(ortalama))

#soru 2
yas_str = input("yaşınıız giriniz: ")
print("gelen veri tipi:", type(yas_str))

yas_int = int(yas_str) 
print( yas_int + 5) # tip dönüşümü ile stringi integera çevirme

#soru 3
ürün_fiyati = input("ürün fiyatını giriniz: ")
kdv = float(ürün_fiyati) * 0.18
toplam_fiyat = float(ürün_fiyati) + kdv
print("KDV:",round(kdv, 2))
print("Toplam Fiyat:",round(toplam_fiyat, 2))

#soru 4
sayilar = [10, 20, 30, 40, 50]
print(sayilar[0]) # 1. eleman
print(sayilar[-1]) # son eleman
print(sayilar[1:]) # 1. indexten sonuna kadar olan elemanlar

sayilar.append(60) # listeye eleman ekleme
print("60 eklendi:", sayilar)

sayilar.remove(20) # listeden eleman silme
print("20 silindi:", sayilar)


#soru 5
koordinat = (12, 34)
x = koordinat[0]
y = koordinat[1]
print("x koordinatı:", x)
print("y koordinatı:", y)
# koordinat[0] = 15 # tuple değiştirilemez, hata verir

#soru 6
ogrenci = {"isim": "Hale", "yas": 22, "bolum": "bilgisayar mühendisliği"}
print(ogrenci["isim"]) # "Hale"
ogrenci["yas"] = 23 # yaş değerini güncelleme

print("güncel sözlük: ", ogrenci)
print("anahtarlar:" , list(ogrenci.keys())) # sözlüğün anahtarlarını liste olarak verir
print("değerler:", list(ogrenci.values())) # sözlüğün değerlerini liste olarak verir

#soru 7
liste = ("hale", "ali", "ayşe","ali")
benzersiz_liste = set(liste) # set() fonksiyonu ile tekrar eden elemanları kaldırır
print(len(benzersiz_liste)) # benzersiz eleman sayısı
