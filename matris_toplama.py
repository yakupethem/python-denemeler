import random

matris1 = [[3 for x in range(3)] for y in range(3)]
matris2 = [[3 for x in range(3)] for y in range(3)]
matrisToplam = [[3 for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        matris1[i][j] = random.randint(0, 5)
        matris2[i][j] = random.randint(0, 5)
        matrisToplam[i][j] = matris1[i][j] + matris2[i][j]
print(matris1)
print(matris2)
print("+","-"*50)
print(matrisToplam)
