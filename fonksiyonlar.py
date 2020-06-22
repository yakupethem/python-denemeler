#girdi = input("metin giriniz: ")

#print(girdi.lower())  #hepsi küçük harfle yazar
#print(girdi.upper())  #hepsi büyük harf yazar

#print(girdi.replace("birmukabele", "bilmukabele"))  #tek harf veya birden fazla kelmeyi değiştirir

"""meyveler = input("meyve giriniz: ")"""
"""print(girdi.split(","))  #girdileri ayrı ayrı listeliyor
for meyve in girdi:
    print(meyve)"""
"""while True:
 aranan_meyve = input("aranacak meyveyi girin: ")
var_mi = aranan_meyve in meyveler
if var_mi == True :
    print(aranan_meyve, "var")
else:
    print("aranan meyve yok")"""

yas =  input("yas: ")
isim = input("isim: ")
tanım = "merhaba ben {} yaşım {}"
print(tanım.format(isim,yas))



