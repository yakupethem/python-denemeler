class Maths:
    def __init__(self, sayi1 , sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2
"""

a = int(input("sayı gir: "))
b = int(input("sayı2 gir: "))

math = Maths(a,b)
print(math.topla())
"""
