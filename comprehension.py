"""
rakamlar=[]
for i in range(10):
    rakamlar.append(i)
sayilarin_karesi = [sayi*sayi for sayi in rakamlar]

cift_sayilar = [ sayi for sayi in rakamlar if sayi % 2 == 0]

tek_sayilar = [ sayi for sayi in rakamlar if sayi % 2 != 0]

print(rakamlar)
print(sayilarin_karesi)
print(cift_sayilar)
print(tek_sayilar)
"""

movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']
#print(list(zip(movies,year)))
yeni_liste = {film:yil for film,yil in zip(movies,year)}
#print(yeni_liste)
yani = [[isim+"'in en sevdiği film "+film+str(yil)+" yılında çıkmıştır."]for isim,film,yil in zip(names,movies,year)]
for sirala in yani:
    print(sirala)