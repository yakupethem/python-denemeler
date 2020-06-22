import random


def frekansBul():
    rastgele = random.randint(-5, 5)
    return rastgele


liste = []
i = 0
while i < 20:
    liste.append(frekansBul())
    i += 1
print("rastgele sayılar:", liste)
pozitifSayiListesi = []
for sayi in liste:
    if sayi > 0:
        pozitifSayiListesi.append(sayi)

en_kucuk = pozitifSayiListesi[0]
for sayi in pozitifSayiListesi:
    if sayi <= en_kucuk:
        en_kucuk = sayi

a = pozitifSayiListesi.count(en_kucuk)

print("en küçük pozitif tam sayı:", en_kucuk)
print("Bu değer ", a, " kere tekrar ediyor")
