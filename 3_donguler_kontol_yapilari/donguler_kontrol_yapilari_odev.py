# soru 1 (if)

print("soru 1 çözümü")
sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

# soru 2 (for) 1 den 10 kadar 10 dahil sayıları yazdırın 
#ayrıca bu sayıkların toplamını yazdırın
print("soru 2 çözümü")
toplam = 0

for i in range(1,11):
    print(i)
    toplam += i # her döngüde toplam değişkenine i değerini ekliyoruz

print("Toplam:", toplam)

#soru 3 (while)
"""
kullanıcıdan "q" yazana kadar sürekli giriş alın.
kullanıcı her giriş yaptığında ekrana "Giriş yapıldı: <girdi>" yazdırın.
kullanıcı "q" yazdığında döngüden çıkın ve ekrana "Program sonlandırıldı." yazdırın.
"""
print("soru 3 çözümü")
giris= ""
while giris != "q":
    giris = input("Bir giriş yapın (çıkmak için 'q' yazın): ")
    if giris != "q":
        print(f"Giriş yapıldı: {giris}")

print("Program sonlandırıldı.")

#soru 4 (nested)
"""
1 den 20 ye kadar olan sayıları dolaşın
eger sayı çift isw "çift" tek ise "tek" yazdırın"
ayRICA SAYI 10 DAN KÜÇÜKSE "küçük/eşit" 10 DAN BÜYÜKSE "büyük" yazdırı
"""
print("soru 4 çözümü")

for sayi in range(1, 21):
    # ilk kontrol: çift mi? tek mi?
    if sayi % 2 == 0:
        print(f"{sayi} çift")
    else:
        print(f"{sayi} tek")

    # ikinci kontrol: 10 dan küçük mü? büyük mü?
    if sayi <= 10:
        print(f"{sayi} küçük/eşit")
    else:
        print(f"{sayi} büyük")