dosya = open("isimler1.txt","w")
print("Ahmet","Mehmet","Sevgi","Sinan","Deniz","Ege","Efe","Ferhat","Fırat","Zeynep","Özhan","Özkan",sep="\n" ,file=dosya)
dosya2 = open("isimler2.txt","w")
print("Gürsel","Mehmet","Sevgi","Sami","Deniz","Efe","Ferhat","Fırat","Tülay","Derya", sep="\n", file=dosya2)
dosya2.close()
dosya.close()

a = open("isimler1.txt")
b = open("isimler2.txt")
dosya_satirler = a.readlines()
dosya2_satirler = b.readlines()
for x in dosya_satirler:
    if not x in dosya2_satirler:
        print(x)

dosya2.close()
dosya.close()