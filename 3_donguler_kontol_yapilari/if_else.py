# if yapısı bir koşulun doğru veya yanlış olmasına göre farklı kod bloklarının çalıştırılmasını sağlar.
"""
if kosul:
    yapilacak_islem
    """
sayi = 10
if sayi > 0: 
    print("Sayı pozitiftir.") 


#if sayi > 0:
#print("burası çalışmaz.")  # indentationError: expected an indented block  girintiye dikkat edilmelidir. if bloğu içindeki kodlar bir tab boşluğu veya dört boşluk ile girintilenmelidir.

# if else yapısı: else koşul yanlış ise çalışır
sayi = -5
if sayi > 0:
    print("Sayı pozitiftir.")
else:
    print("Sayı negatiftir veya sıfırdır.")

#if elif else yapısı: birden fazla koşul kontrolü yapmak için kullanılır.
ogrenci_notu = 85
if ogrenci_notu >= 90:
    print("Notunuz: A")
elif ogrenci_notu >= 80:
    print("Notunuz: B")
else:
    print("Notunuz: C") 

meyveler = ["elma", "muz", "çilek"]
urun = input("Bir meyve girin: ")

if urun in meyveler:
    print("Meyve mevcuttur.")
else:
    print("Meyve mevcut değildir.")