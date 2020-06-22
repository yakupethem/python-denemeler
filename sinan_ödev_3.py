import random
def frekansBul():
    rastgele = random.randint(0,100)
    return rastgele
liste = []
i = 0
while i < 20:
    liste.append(frekansBul())
    i += 1
print("Notlar: ", liste)
en_kucuk = liste[0]
en_buyuk = liste[0]
toplam=0
ortalama = toplam/len(liste)
for sayi in liste:
    toplam += sayi
    if  sayi <= en_kucuk:
        en_kucuk = sayi
    if sayi >= en_buyuk:
        en_buyuk = sayi
ortalama = toplam/len(liste)
print("en yüksek not:",en_buyuk,"en düşük not: ",en_kucuk,"ortalama: ",ortalama)
