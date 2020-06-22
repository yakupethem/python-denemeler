import random, string
"""
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
"""
rastgele = string.ascii_letters + string.digits
sifre = ""
for i in range(7):
    sifre += random.choice(rastgele)
print(sifre)

sifre2 = random.choices(rastgele,k=7)
print(sifre2)

sifre3 = "".join(random.sample(rastgele,7))
print(sifre3)