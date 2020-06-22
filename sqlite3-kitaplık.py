import sqlite3

baglan=sqlite3.connect("kitaplık.sqlite")
cursor=baglan.cursor()

cursor.execute("create table if not exists kitaplar (kitap adı text,yazarı text,sayfa_sayısı int)")

#cursor.execute("insert into kitaplar values ('suç ve ceza','dostoyevski',480)")
#cursor.execute("insert into kitaplar values('beyaz diş', 'jack london' ,300)")
cursor.execute("select * from kitaplar")
baglan.commit()

veri=cursor.fetchall()
a=0
for i in veri:
        print("kitabın adı:",i[a])
        a+=1
        print("kitabın yazarı:", i[a])
        a+=1
        print("sayfa sayısı:", i[a])
        a=0
        print("---------------")