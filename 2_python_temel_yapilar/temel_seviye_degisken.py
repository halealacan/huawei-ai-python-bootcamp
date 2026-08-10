# degisken kavramı
"""
integer,float,string
type  fonksiyonu ve veri tipi kontrolü
tip dönüşümleri
listeler
indeksleme ve slicing
liste metodları
tuple
sözlük
set
veri yapıları arasındaki farklar
"""

#ctrl + ö ile yorum satırı açıp kapatma

# #integer:
# yas = 22
# print(yas)
# # zam uygıulaması
# birim_fiyat = 10 
# yüzde =int(input("Yüzde girin: "))
# print(yüzde)
# zamli_fiyat = birim_fiyat + birim_fiyat*yüzde/100
# print(zamli_fiyat)

#float: 
# fiyat = 0.1 + 0.244444444
# print(fiyat)

# print(round(fiyat,2)) # yuvarlama işlemi 

# #proje: gelen fiyat üzerinden kdv (%20) hesaplama
# fiyat = float(input("fiyat girin: "))
# print(fiyat)
# kdvli_fiyat = fiyat + fiyat* 0.20
# print(kdvli_fiyat)

# string:
isim = "hale"
print(isim)
sirket_adi = "abc"
kurulum_yili = 2026

# stringle sayı toplanmaz
# print(sirket_adi + kurulum_yili) # hata verir
# print( " kurulum yılı: " + str(kurulum_yili)) # tip dönüşümü ile stringe çevirme
print(f"şirket adı: {sirket_adi} kurulum yılı: {kurulum_yili}") # f-string kullanarak birleştirme

#lower() ve upper() metodları
print(isim.lower())
print(isim.upper())

#len() fonksiyonu
print(len(isim)) # isim değişkeninin uzunluğunu verir

#yer değiştirme
metin = "merhaba"
print(metin.replace("m", "M")) # m harfini M ile değiştirir

# !!! input default olarak string tipinde veri alır, toplamada kullanmak için tip dönüşümü gerekir

# print(int("abc")) # hata verir, string tipinde sayı olmayan bir veri tipini int() ile dönüştürmeye çalıştık

#listeler:
liste = [1,2,3,4,5]
isimler = ["ali", "veli", "ayşe"]
karma_liste = [1, "ali", 3.14, True]

print(len(liste)) # listenin uzunluğunu verir

# listelelrde slicing 
sayilar = [1,2,3,4,5,6,7,8,9]
print(sayilar[0:5]) # 0. indexten 5.
print(sayilar[2:7]) # 2. indexten 7. (2. index dahil, 7. index dahil değil)

#listeye eleman ekleme 
sayilar=[1,2,3,4,5]

sayilar.append(6)
print(sayilar) # [1, 2, 3, 4, 5, 6]

sayilar.insert(2, 2.5) # 2. indexe 2.5 ekler
print(sayilar) # [1, 2, 2.5, 3, 4, 5, 6]

sayilar.remove(2.5) # 2.5 değerini listeden siler

sayilar.pop() # son elemanı siler
sayilar.pop(0) # 0. indexteki elemanı siler beelirli bir indexteki elemanı silmek için pop() metodunu kullanabiliriz

sayilar.sort() # listeyi küçükten büyüğe sıralar
sayilar.reverse() # listeyi tersine çevirir

sayilar[0] = 999 # 0. indexteki elemanı 999 ile değiştirir


#tuple: değiştirilemez veri tipidir, listeden farkı budur
koordinatlar = (10, 20)
renkler = ("kırmızı", "mavi", "yeşil")

# list vs tuple
list = [1,2,3]
liste[0] = 999 # listelerde eleman değiştirilebilir

tup = (1,2,3)
# tup[0] = 999 # tuples are immutable, this would cause an error

# indeksleme ve slicing liste ile aynı mantıkta çalışır

#tek elemanlı tuple
x = (5,) # tek elemanlı tuple oluşturmak için virgül kullanılır
x =(5) # bu bir integerdır, tuple değildir

#tuple ununpacking
koordinatlar = (10, 20)
x, y = koordinatlar # x=10, y=20 olur
print(x)
print(y)

#tuple metodları: count() ve index()
t = (1,2,3,1,2,1)
print(t.count(1)) # 1 sayısının kaç kez geçtiğini sayar
print(t.index(2)) # 2 sayısının ilk geçtiği indeksi verir

#dictionary: key-value pairs
ogrenci = {"isim": "hale", "yas": 22, "not": 85}
print(ogrenci["isim"]) # hale
print(ogrenci["yas"]) # 22
print(ogrenci["not"]) # 85

#yeni değer ekleme
ogrenci["cinsiyet"] = "kız" # yeni key-value çifti ekler

#güncelleme
ogrenci["not"] = 90 # not değerini günceller
print(ogrenci["not"]) # 90

#eleman silme
del ogrenci["cinsiyet"] # cinsiyet key-value çiftini siler
print(ogrenci) # {'isim': 'hale', 'yas': 22, 'not': 90}

 #anahtar ve değerleri alma
print(ogrenci.keys()) # dict_keys(['isim', 'yas', 'not'])
print(ogrenci.values()) # dict_values(['hale', 22, 90])
print(ogrenci.items()) # dict_items([('isim', 'hale'), ('yas', 22), ('not', 90)])


#set: benzersiz elemanlardan oluşan bir veri tipidir, aynı eleman birden fazla kez eklenemez
meyveler = {"elma", "armut", "muz"}
sayilar = {1,2,4,5}
print(meyveler) # {'elma', 'armut', 'muz'}
print(sayilar) # {1, 2, 4, 5}

sayilar={1,2,3,4,5,5,5,5} 
print(sayilar) # {1, 2, 3, 4, 5} aynı eleman birden fazla kez eklenemez

# setlerin index yani sırası yoktur
#print(meyveler[0]) # hata verir, setlerde indexleme yoktur


union = {1,2,3}.union({3,4,5}) # iki setin birleşimi
print(union) # {1, 2, 3, 4, 5}

intersection = {1,2,3}.intersection({3,4,5}) # iki setin kesişimi
print(intersection) # {3}

difference = {1,2,3}.difference({3,4,5}) # ilk setin ikinci setten farkı
print(difference) # {1, 2}

