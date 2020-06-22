import random
def loto():
    rastgele = random.randint(1, 49)
    return rastgele
x=1
while x <=8 :
    print(x, ". Kolon: ")
    y = 1
    while y <= 6 :
        print(loto())
        y += 1
    x += 1



