"""
Bozuk veri temizleme
veri:
        70
        85
        abc
        90
        50
        hata
        60
Amaç:
    - dosyayı oku
    - sayıya çevrilemeyen satıları atla
    - geçerli notları topla
    - ortalama hesapla
"""

def ortalama_hesapla(dosya_yolu):
    sayilar = []

    with open(dosya_yolu, "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()
            if not satir:
                continue

            try:
                sayi = float(satir)   # notlar tam sayıysa int de kullanılabilir
                sayilar.append(sayi)
            except ValueError:
                # "abc", "hata" gibi sayıya çevrilemeyenleri atla
                continue

    if not sayilar:
        return None  # hiç geçerli veri yoksa

    return sum(sayilar) / len(sayilar)


print(ortalama_hesapla("notlar.txt"))