sayilar = [1, 2, 5, 8, 9]
#  kullanıcıdan sayı iste sayının yukarıda olduğunu kontrol et
istenen_sayi = int(input("sayı giriniz: "))  # metin olarak gelir
sayi_varmi = False
sayi_sirasi = 1
for sayi in sayilar :
    if sayi == istenen_sayi:
        sayi_varmi = True
        break
        #print("sayı var")
    elif sayi > istenen_sayi :
        break
    sayi_sirasi += 1
    if sayi_varmi == True :
        print("sayı dizide var ", sayi_sirasi, ". sırada")
    else:  # else bi kere yazılır şartlar olmazsa
        print("sayı bulunamadı ", "olsaydı", int(sayi_sirasi), "olacaktı")


