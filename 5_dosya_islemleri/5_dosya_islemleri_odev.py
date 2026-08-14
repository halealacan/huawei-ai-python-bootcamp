# SORU 1
# "notlar.txt" adında bir dosya oluşturun ve içine
# 5 öğrencinin notunu yazın. Her not ayrı satırda olsun.

notlar = [55, 70, 85, 60, 92]

with open("notlar.txt", "w", encoding="utf-8") as f:
    for notu in notlar:
        f.write(f"{notu}\n")

print("notlar.txt oluşturuldu ve notlar yazıldı.")

# SORU 2
# Bu dosyayı okuyun ve:
# - Notların ortalamasını hesaplayın
# - En yüksek notu bulun
# - En düşük notu bulun

with open("notlar.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Her satırı int'e çevir
notlar = [int(line.strip()) for line in lines]

ortalama = sum(notlar) / len(notlar)
en_yuksek = max(notlar)
en_dusuk = min(notlar)

print("Notlar:", notlar)
print("Ortalama:", ortalama)
print("En yüksek not:", en_yuksek)
print("En düşük not:", en_dusuk)
 


# SORU 3
# Eğer ortalama 50'den büyükse "Sınıf geçti"
# değilse "Sınıf kaldı" sonucunu
# "sonuc.txt" dosyasına kaydedin.
 
with open("notlar.txt", "r", encoding="utf-8") as f:
    notlar = [int(line.strip()) for line in f.readlines()]

ortalama = sum(notlar) / len(notlar)

sonuc = "Sınıf geçti" if ortalama > 50 else "Sınıf kaldı"

with open("sonuc.txt", "w", encoding="utf-8") as f:
    f.write(sonuc)

print("sonuc.txt yazıldı:", sonuc)