class Kimlik:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas


class Personel(Kimlik):

    def __init__(self, ad, soyad, yas, birim):
        super().__init__(ad, soyad, yas)
        self.birim = birim


memur1 = Personel("yakup", "türkyılmaz", 26, "ARGE")
memur2 = Personel("ali", "veli", 49, "Üretim")
memur3 = Personel("cansu", "cansu", 25, "İnsan Kaynakları")

dosya = open("çalışanlar.txt", "w")
# print(memur1, file=dosya)

print("memurun adı: ", memur1.ad, file=dosya)
print("memurun yaşı: ", memur1.yas, file=dosya)
print("memurun çalıştığı birimi: ", memur1.birim, file=dosya)

dosya.close()
