sesli_harfler = "aeıioöuü"

metin = input("metin girin: ")
sayac = 0
tekrarlar = []
#metin = "yakup"
for harf in metin.lower():
    if  harf in tekrarlar:
        continue
    if  harf in sesli_harfler:
        sayac +=1
        tekrarlar.append(harf)
       # print(harf)
print("metinde ",sayac, "adet sesli harf vardır.Bunlarda; " , tekrarlar)
#   print(tekrarlar)



