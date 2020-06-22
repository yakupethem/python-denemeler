sayi = int(input("sayı giriniz = "))
baslangic = 1
if sayi < 0 :
        print("negatif sayının faktöriyeli olmaz")
elif sayi == 0 :
        print(baslangic)
else:
        for x in range(1,sayi+1):
            baslangic = baslangic * x
        print("sayının faktöriyeli = ", baslangic)
