import sqlite3

baglanti=sqlite3.connect("SQLite-dersler.sqlite")
cursor=baglanti.cursor()

def tablo_olustur(kitap_adi="",yazar="",sayfa="",durum=""):
    cursor.execute("create table if not exists kitaplık_prgramı(ID int primary key AUTOINCREMENT,kitap_adı ,"
                   "yazar ,sayfa int,durum )")
    cursor.execute("insert into kitaplık_prgramı(kitap_adı,yazar,sayfa,durum) values('"+kitap_adi+"','"+yazar+"','"+sayfa+"','"+durum+"')")
    baglanti.commit()
def tablosil():
    cursor.execute("drop table ogrenciler")
    baglanti.commit()
def verigetir():
    cursor.execute("select * from kitaplık_prgramı")
    veri=cursor.fetchall()
    a = 0
    for i in veri:
        print("kitabın adı:", i[a])
        a += 1
        print("kitabın yazarı:", i[a])
        a += 1
        print("sayfa sayısı:", i[a])
        a+=1
        print("okunma durumu:", i[a])
        a = 0
        print("---------------")
def verisil(kitap_adi):
    cursor.execute("delete from kitaplık_prgramı where kitap_adı='"+kitap_adi+"'")
    baglanti.commit()
def tabloguncele(kitap_adi):
    cursor.execute("update ogrenciler set notu=100 where kitap_adı='"+kitap_adi+"'")
    baglanti.commit()
