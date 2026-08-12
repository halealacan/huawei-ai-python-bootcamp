#fonk tanımlandı
def selam_ver():
    print("hi!")

#çağırma:
selam_ver()

#parametre kullanımı
def selam_ver(isim): 
    print(f"merhaba ben {isim} akıllı asistanıyım")

selam_ver("türkiye yapay zeka akademisi")


def topla(a,b):
    sonuc = a +  b
    print(f"sonuc: {sonuc}")
    return sonuc

topla(5,3)