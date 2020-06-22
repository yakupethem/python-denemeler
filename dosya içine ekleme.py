dosya = open("örnekdosya.txt","w")
dosya.write("muslera\n")
dosya.write("seri\n")
dosya.write("falcao\n")

dosya.close()

with open("örnekdosya.txt","r+")as dosya:
    oku = dosya.readlines()  #readlines liste haline getirir
    oku.insert(1,"donk\n")  # oku listesinin 1. indexine yazar
    dosya.seek(0)  # 0. satıra gider
    dosya.writelines(oku)  #listeyi dahil eder