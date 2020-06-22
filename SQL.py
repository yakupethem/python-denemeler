from pypyodbc import *

baglanti = connect('driver={sql server};server=DESKTOP-EECN01E\SQLEXPRESS;'
                   'database=örnek11;trusted_connection=true')

araci=baglanti.cursor()  #Veritabanı bağlantısı ile komutlarımızı gönderebilmek için aracı bir imleç oluşturmamız gerekiyor.

araci.execute('select * from product where unitprice<20')
#dönen sonuçları (dizi olarak döner) bir değişkene aktarmamız gerekiyor

kayitlar=araci.fetchall()
# sıra ekrana yazdırmaya geldi
#for kayit in kayitlar:
    #print(kayit)
    #print("-------------------------------------")
araci2=baglanti.cursor()
#araci2.execute('insert into örnek10.dbo.employes values(?,?,?,?,?)', ["yakoş","male","5500","aasdf@asdf.com","TR"])
#araci2.execute('delete from örnek10.dbo.employes where ıd=11')
#araci2.execute('update örnek10.dbo.employes set salary=1000 where ıd=7')
#araci2.execute('select * from örnek10.dbo.employes')
#araci2.execute('create table python(id int,name nvarchar(20))')
#araci2.commit()  # tabloyu yaptığım değişikliği onaylıyoruz demek.commit yapmazsak insert olmaz
kayitlar2=araci2.fetchall()

for kayit in kayitlar2:
    print(kayit)
baglanti.close()