from youtubeClassOrnekdevam import Sinav

sorular = [
    "Osmanlı'nın ilk anayasası hangisidir? \na)senedi ittifak\nb)kanuni esasi\nc)1921 anayasası\n\n ",
           "TC tarihinde kaç anayasa vardır? \na)3\nb)4\nc)5\n\n ",
           "Şuanda CB seçimi kaç yılda bir yapılı? \na)3\nb)4\nc)5\n\n "
]

sinavFonk = [
    Sinav(sorular[0],"b"),
    Sinav(sorular[1],"a"),
    Sinav(sorular[2],"c"),
]
def calistir(sinavFonk):
    puan = 0
    for x in sinavFonk:
        cevapp = input(x.soru+"cevabın: ")
        if  cevapp.lower() == x.cevap:
            puan += 1
    print("Aldığın Puan: ",puan)
    print(len(sorular)," sordudan ", puan," doğrun var.")
calistir(sinavFonk)


