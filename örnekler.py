"""print("www" , " python","com")
print("www" , "python","com", sep =".")
print("bir","iki","üç","dört","ondört","", sep=" mumdur ")  #sep= aralara işlem yapar
#print("bir","iki","üç","dört","ondört","", sep=None , sep="mumdur" ) iki tane sep olmuyor
print("birinci satır","ikinci satır","üçüncü satır",sep="\n")  # \n satırbaşı ifadesi
print("bir","iki","üç","dört","ondört","",sep=" mumdur ",end="\n")

dosya = open("deneme.txt","w")  # w karakteri açtığımız dosyayı yazma moduna çevirdi
print("burada yeni dosya açtık",file=dosya)
dosya.close()
#import os
#os.getcwd()  # Bu komutun çıktısında hangi dizinin adı görünüyorsa, deneme.txt dosyası da o dizidedir

dosya = open("deneme2.txt","w")
print("artık deneme dosyasına başka yerden ekleme yapabiliriz",file=dosya)
dosya.close()  # dosyayı kapatmayı unutma

a=open("deneme3.txt","w")
print("dosya açmaya dpyamadık",file=a)
a.close()"""

"""print("Çarpım Programı")
print("_"*10)
ilk_sayi = int(input("ilk sayıyı giriniz: "))
ikinci_sayi = int(input("ikinci sayıyı giriniz: "))
print(ilk_sayi,"X",ikinci_sayi,"=",ilk_sayi*ikinci_sayi)"""

# sayı = int(input("1-10 arası sayı giriniz: "))  input whilenin üstünde olunca döngü sonsuza gidiyor
"""while True:
    sayi = int(input("1-10 arası sayı giriniz: "))
    if  sayi>10:
     print("sayı 10 dan küçük olmalı")
     continue
    elif sayi<1:
     print("sayı 1 den büyük olmalı")
     continue
    else:
        print("tebrikler")
        break"""
"""dosya_ac= open("deneme3.txt","w")
print(*"yakocan40",sep="\n",file=dosya_ac , flush=True)
print("atkafasi", sep="+", file=dosya_ac , flush=False)
dosya_ac.close()"""
"""print("istanbul\'un havası çok güzel")

print("pythonun adı \"piton\" yılanından gelmez")

yazi ="işte şimdi sıçtınız"
print(yazi,"\n","-"*len(yazi), sep="")
print("\a")"""

"""import unicodedata
print(unicodedata.name("a"))  modul çağırıp a harfinin latin tanımını getirir"""


