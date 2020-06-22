import random
rastegele_sayi = random.randint(1,10)  #1 random sayı 1 ile 10 arası
print(rastegele_sayi)
sayac = 0
"""tahmin =input("1-10 arasında bir sayı giriniz: ")  #burayı dahil edincce sonsuza gidiyor
tahmin_sayi = int(tahmin)"""
while True:
    tahmin = input("1-10 arasında bir sayı giriniz: ")
    tahmin = tahmin.strip()  # boşlukları yok eder
  #  if len(tahmin) > 0 and tahmin.isdigit():  #boşluk veya harf girmyi önlemek için , isdigit sayı mı demek
   #     tahmin = input("1-10 arasında bir sayı giriniz: ")
    tahmin_sayi = int(tahmin)
    sayac += 1
    if tahmin_sayi == rastegele_sayi :
        print("TEBRİKLER sayıyı buldunuz: ", rastegele_sayi )
        break
    elif tahmin_sayi < rastegele_sayi :
        print("sayınızı artırın")
        continue
    elif tahmin_sayi > rastegele_sayi :
        print("sayınızı azaltın")
        continue
print(sayac, "kerede buldunuz")









