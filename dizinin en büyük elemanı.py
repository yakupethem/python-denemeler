dizi = [65, 13, 4, 121, 8, 25, 100, 36, 1, 45, 12]
dizi_uzunlugu = len(dizi)
en_buyuk = int(dizi[0])
a = 0
while a <= dizi_uzunlugu-1:
    if en_buyuk <= int(dizi[a]):
        en_buyuk = int(dizi[a])
    a += 1
print(en_buyuk)

for sayi in dizi:
    if  sayi>=en_buyuk:
        en_buyuk=sayi
print(en_buyuk)









