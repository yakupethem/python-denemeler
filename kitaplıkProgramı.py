import SQLite3
import sys

print("programa hoşgeldiniz")
print("-"*50)
while 1==1:
    print("kitalığa ekleme yapmak için E,silmek için S,görüntülemek için G,çıkmak için Ç ye basın: ")
    islem = input()
    if islem.upper()=="E":
        kitap_adi=input("kitap adını girin: ")
        yazar=input("yazarını girin: ")
        sayfa=input("sayfa sayısını girin: ")
        durum=input("kitap okundu mu ?: ")
        SQLite3.tablo_olustur(kitap_adi,yazar,sayfa,durum)
    elif islem.upper()=="S":
        sil=input("silmek istediğiniz kitap_adını girin: ")
        SQLite3.verisil(sil)
    elif islem.upper()=="G":
        SQLite3.verigetir()
    else:
        SQLite3.baglanti.close()
        print("Çıkış Yapıldı İyi Günler")
        sys.exit()


