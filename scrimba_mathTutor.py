#import modules
from  random import randint as r
from time import time as t
# ask how many questions user wants
kacSoru = int(input("kaç soru istersin: "))
enBuyuksayi = int(input("en büyük sayı ne olsun: "))
#set score start at zero
puan = 0
basla =t()
liste = []
#loop through number of questions
for x in range(1,kacSoru+1):
    sayi1, sayi2 = r(1,enBuyuksayi),r(1,enBuyuksayi)
    cevap = sayi1 *sayi2
    cevabin = int(input(f" {sayi1} X {sayi2}: "))
    liste.append(f"{sayi1} X {sayi2} = {cevap}  sen:{cevabin}")
    if  cevabin == cevap:
        puan += 1
    bitir=t()
print("***********************************")

for a in liste:
    print(a)
print(f'{kacSoru} soruda {puan} doğru yaptın.Zamanın :{round(bitir-basla,1)} saniye')
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score

