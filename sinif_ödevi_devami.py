from sinif_ödevi import Personel

dosya = open("çalışanlar.txt","a")

memur_ekle = Personel("radamel","falcao",34,"Forvet")

print("memurun soyadı: ",memur_ekle.soyad,file=dosya)
print("memurun yaşı: ",memur_ekle.yas, file=dosya)
print("memurun mevkisi: ",memur_ekle.birim,file=dosya)

dosya.close()
