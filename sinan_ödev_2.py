def birimAyristir():
    girilen_miktar = int(input("miktarı giriniz(KB): "))
    a = girilen_miktar // 1048576
    b = (girilen_miktar % 1048576)//1024
    c = (girilen_miktar % 1048576)%1024

    print("girilen miktar",a," GB ",b," MB ",c,"KB a karşılık gelir")


birimAyristir()
