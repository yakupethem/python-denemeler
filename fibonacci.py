kacSeri = int(input("kaç seri: "))
basla = 0
ilk_Sayi = int(input("başlamak istedeğiniz sayı: "))
fib_list = [ilk_Sayi]
for i in  range(kacSeri):
    fib = ilk_Sayi + basla
    basla = ilk_Sayi
    ilk_Sayi = fib
    fib_list.append(fib)
print(fib_list)


