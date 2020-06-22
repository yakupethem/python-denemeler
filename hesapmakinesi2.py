import hesap_makinesi_sınıfı
import class2

print("operasyonlar:"
      "1:topla"
      "2:çıkart"
      "3:çarp"
      "4:böl")
a = input("yapacağınız işlemi seçin: ")
operator = int(a)
x = int(input("ilk sayı:"))
y = int(input("ikinci sayı: "))
k = hesap_makinesi_sınıfı.hesapMakinesi(x,y)
m = class2.Maths(x,y)
if operator == 1:
    print("sayıların toplamı: ",m.topla())
elif operator == 2:
    print("sayıların farkı: ",m.cikar())
elif operator == 3:
    print("sayıların çarpımı: ",k.carp())
elif operator == 4:
    print("sayıların bölümü: ",k.bol())
else:
    print("geçersiz operatör")

