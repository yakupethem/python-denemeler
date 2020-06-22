ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
"""tekrarlar = []
for x in ilk_metin:
    if  x in tekrarlar:
        break
    for y in ikinci_metin:
        if x == y :
            continue
        else:
            tekrarlar.append(x)
            #print(tekrarlar)
            break
print(tekrarlar)"""
tekrar = ""
for x in ilk_metin:
    if  x in    tekrar:
        continue
    if  not x   in  ikinci_metin:
        tekrar += x
print(tekrar)