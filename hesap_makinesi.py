import sinif

print("operasyonlar:",
      "1:topla",
      "2:çıkart",
      "3:çarp",
      "4:böl", sep="\n")
a =input("yapacağınız işlemi seçin: ")
operator = int(a)
x = int(input("ilk sayı:"))
y = int(input("ikinci sayı: "))

islem = sinif.Matemetik()


if  operator == 1 :
    print("Toplam: ", islem.topla(x,y))
elif operator == 2:
    print("farkı: ", islem.cikart(x,y))
elif operator == 3:
    print("çarpım: ", islem.carp(x, y))
elif operator == 4:
    print("bölüm: ", islem.bol(x, y))
else:
    print("geçersiz operatör")

