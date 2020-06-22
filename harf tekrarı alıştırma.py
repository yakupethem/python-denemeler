harfler = ["a", "b", "c", "d", "z", "c", "b"]
tekraredenharfler = []
for harf in harfler:
    if  harf in tekraredenharfler:
        break
    sayac = 0
    for tekrar in harfler:
        if tekrar == harf:
            sayac += 1
        if sayac == 2 :
            print(tekrar , "tekrar ediyor")
            tekraredenharfler.append(harf)
            break