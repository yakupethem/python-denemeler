import datetime

def yas_hesapla(dogum_yili):
    current_datetime = datetime.datetime.now() #  sağtıkla go to decralitaion nerden geldiğini gösterir
    #print(current_datetime)
    #print(current_datetime.year)
    yas = current_datetime.year - dogum_yili
    #print(yas)
    return yas

yas_hesapla(1994)

def dizi_ortalaması(dizi):
    toplam = 0
    uzunluk = len(dizi)
    for sayi in dizi:
        toplam += sayi
    return toplam / uzunluk

def tarih_uyarla(tarih):
    str_tarih = tarih.strftime("%x")
    ay_gun_yil = tarih.split("/")
    gun_ay_yil = ay_gun_yil[1], "/", ay_gun_yil[0], "/", ay_gun_yil[2]
    return gun_ay_yil


