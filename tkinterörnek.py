from tkinter import *
from tkinter.ttk import *


def sec():
    # print(combo.get())
    sonuc = Label(text=combo.get()).place(x=10, y=50, width=100)
    sonuc1 = Label(text=c1.get()).place(x=100, y=100, width=100)
    sonuc2 = Label(text="radio seçimi" + str(r.get())).place(x=130, y=50, width=100)


def renk():  # rgb: red blue green
    r = red_spin.get()
    b = blue_spin.get()
    g = green_spin.get()
    # 16lık hex koda dönüştürme
    rh = hex(int(r))  # 0x5
    bh = hex(int(b))
    gh = hex(int(g))
    color = "#" + rh.replace("0x", "") + gh.replace("0x", "") + bh.replace("0x", "")
    print(color)
    pencere.configure(bg=color)  # 6b3


pencere = Tk()

pencere.title("yakocan40")
pencere.geometry("500x300+700+200")
"""
yazi = Label(text="ilk başlık", bg="red", font="Verdana 22 bold")
yazi.pack(side="left")  # top, left, right, bottom
yazi2 = Label(text="ikinci başlık", bg="green", font="Verdana 22 bold")
yazi2.pack(side="left")
yazi3 = Label(text="üçüncü başlık", bg="blue", font="Verdana 22 bold")
yazi3.pack(fill="x")  # x, y
yazi4 = Label(text="dördüncü başlık", bg="yellow", font="Verdana 22 bold")
yazi4.pack(expand="no")  # yes, no
# pack() komponentleri paketliyor
# grid() arayüzü parçalara bölüyor kare kare
# place() x,y koordinatlarıyla yerletiiriyor

yazi = Label(text="ilk başlık", bg="red", font="Verdana 22 bold")
yazi.grid(row=1, column=5)
yazi2 = Label(text="ikinci başlık", bg="yellow", font="Verdana 22 bold")
yazi2.grid(row=5, column=5)

yazi = Label(text="ilk başlık", font="Verdana 22 bold",bg="red")
yazi.place(x=150, y=50)
yazi2 = Label(text="ikinci başlık", bg="yellow", font="Verdana 22 bold")
yazi2.place(x=30, y=90)


combo = Combobox()
combo["values"] = ("bir şehir seçin", "istanbul", "ankara", "bursa", "eskişehir", "kırşehir")
combo.current(0)
combo.place(x=10, y=10)

buton = Button(text="seç", command=lambda: sec()).place(x=160, y=8)
c1 = StringVar()
cb = Checkbutton(text="seç tuşu", variable=c1, onvalue="seçili", offvalue="seçili değil", command=sec).place(x=20,
                                                                                                             y=100)
r = IntVar()
rb = Radiobutton(text="radyo tuşu", variable=r, value=1, command=sec).place(x=200, y=100)
rb2 = Radiobutton(text="radyo tuşu2", variable=r, value=2, command=sec).place(x=200, y=130)
"""

red_label = Label(text="kırmızı")
red_label.place(x=20, y=20)
red_spin = Spinbox(from_=0, to=15, width=10, command=renk)
red_spin.place(x=80, y=20)

green_label = Label(text="yeşil")
green_label.place(x=20, y=50)
green_spin = Spinbox(from_=0, to=15, width=10, command=renk)
green_spin.place(x=80, y=50)

blue_label = Label(text="mavi")
blue_label.place(x=20, y=80)
blue_spin = Spinbox(from_=0, to=15, width=10, command=renk)
blue_spin.place(x=80, y=80)

pencere.mainloop()
