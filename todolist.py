import os
#operating system
import fileinput
from os import path
import re

# bir dosya içerisinde belli bir metni bulup başka bir metin ile değiştiren fonksiyon
def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

dosyaVarMi = path.exists("yapılacaklarListesi.txt")

if  dosyaVarMi == False:
    dosya = open("yapılacaklarListesi.txt","w")
    dosya.close()
dosya = open("yapılacaklarListesi.txt","r")
print("işler: ")
print(dosya.read())
dosya = open("yapılacaklarListesi.txt","r")
is_sayisi = len(dosya.readlines())
dosya.close()

istek = input("dosyaya eklemek için: 'E'"
              "dosyadan tamamlamak için: 'T'ye basın: ")

if istek.upper() == "E":

    ekle = input("eklemek istediğin işi yazın: ")
    dosya = open("yapılacaklarListesi.txt", "a")
    if is_sayisi>0:
        dosya.write("\n")
    dosya.write(str(is_sayisi+1))
    dosya.write(".")
    dosya.write(ekle)

elif istek.upper() == "T":

    tamamla = int(input("tamamlamak istediğiniz işin numarasını yazın: "))
    dosya = open("yapılacaklarListesi.txt", "r+")
    veri = dosya.read()
    isler = dosya.readlines(tamamla-1)
    tamam=str(isler)+"tammalandı"
    dosya.seek(tamamla)
    dosya.writelines(tamam)
else:
    print("Bu numarada iş yok")



