import datetime

x = datetime.datetime.now()
tarih = (x.strftime("%x"))
ay_gun_yil = tarih.split("/")
gun_ay_yil = ay_gun_yil[1] , "/" , ay_gun_yil[0] , "/" , ay_gun_yil[2]

print(x.strftime("%x"))
print(gun_ay_yil)
print(ay_gun_yil)