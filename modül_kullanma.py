from datetime import datetime

import araçlar  #from araçlar import def adı / önce modülü import et

dogum_yili=int(input("doğum yılınızı girin: "))
yas = araçlar.yas_hesapla(dogum_yili)
print("yaşınız: ", yas)

#dizi = [2,13,6]
sayi1=int(input(("sayı: ")))
sayi2=int(input(("sayı: ")))
sayi3=int(input(("sayı: ")))
dizi=[sayi1,sayi2,sayi3]
ortalama = araçlar.dizi_ortalaması(dizi)
print("dizinin ortalaması:  ", round(ortalama))  #raund yuvarlıyor


from araçlar    import tarih_uyarla
a = tarih_uyarla(datetime.now())
print(a)

