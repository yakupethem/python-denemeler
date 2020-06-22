class Person:
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
class Calisan(Person):
    def __init__(self, maas, ad, soyad, yas):
        super().__init__(ad, soyad, yas)
        self.maas = maas

class Musteri(Person):
    def __init__(self, kredikartno, ad, soyad, yas):
        super().__init__(ad, soyad, yas)
        self.kredikartno = kredikartno

ahmet = Musteri(232323,"ahmet","mehmet",32  )
mehmet = Calisan(1000,"ali","veli",42)
print(ahmet.ad,"'in kredi kartı numarası: ",ahmet.kredikartno)
print(mehmet.ad,"'in maaşı: ",mehmet.maas)

