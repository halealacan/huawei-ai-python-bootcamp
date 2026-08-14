"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""

class VeriAnalizi:
    def __init__(self, veriler):
        self.veriler = veriler

    def toplam_hesapla(self):
        return sum(self.veriler)

    def ortalama_hesapla(self):
        return self.toplam_hesapla() / len(self.veriler) if self.veriler else None

    def max_deger(self):
        return max(self.veriler) if self.veriler else None

    def min_deger(self):
        return min(self.veriler) if self.veriler else None


# Veriler: [10, 20, 30, 40, 50]
veriler = [10, 20, 30, 40, 50]
analiz = VeriAnalizi(veriler)

toplam = analiz.toplam_hesapla()
ortalama = analiz.ortalama_hesapla()
maksimum = analiz.max_deger()
minimum = analiz.min_deger()

print("Toplam:", toplam)         
print("Ortalama:", ortalama)     
print("Maksimum değer:", maksimum)  
print("Minimum değer:", minimum)    
