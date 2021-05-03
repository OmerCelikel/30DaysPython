"""

TAŞ KAĞIT MAKAS OYUNU

"""


# Yenenler     Taş Makası , Kağıt Taşı , Makas Kağıdı
# Yenilenler   tam tersi


# Tkinter ile yapılacak
# random kullanılacak

#Importing Libraries (Kütüphaneleri Ekledik)
from tkinter import *
import  random



#Penceremizi oluşturma

root = Tk()
root.geometry('400x400')
root.resizable(0,100)
root.title('Taş,Kağıt, Makas')
root.config(bg='gray24')

#Label oluşturacağız bunu kullanıcı değiştiremeyecek

my_label = Label(root,text ="Taş , Kağıt , Makas" , font='arial 18 bold', bg='snow').pack()
#my_label.pack(side="top")
#can.place(relx=0.5, rely=0.5, anchor=CENTER)

#Kullanıcı Seçimi , Entry Widget ı input alacak
user_take = StringVar()
user_option = Label(root,text = "Birini seç : taş  kağıt  makas", font='arial 14 bold', bg='snow').place(x = 65 , y = 70)
Entry(root,font = "arial 15", textvariable = user_take , bg = "antiquewhite2").place(x=85 , y = 130)

#bilgisayar Seçimi
resultComputer = StringVar()
#burada 3 seçenek var bilgisayarın seçeceği random olarak bilgisayara seçtiriyoruz
comp_pick = random.randint(1,3) #  1 2 3 Taş Kağıt Makas
if comp_pick == 1:
    comp_pick = 'taş'
    resultComputer.set("taş")

elif comp_pick == 2:
    comp_pick = "kağıt"
    resultComputer.set("kağıt")
else:
    comp_pick == "makas"
    resultComputer.set("makas")


#bilgisayarın seçimini görebilirsiniz
#print(comp_pick)


#oyunu başlatalım
result = StringVar()

def play():
    #kullanıcının seçimini getirdik
    user_pick = user_take.get()
    if user_pick == comp_pick:
        result.set("Kazanan yok, berabere")
    elif (user_pick == 'taş' and comp_pick == "makas") or (user_pick == 'kağıt' and comp_pick == "taş") or \
            (user_pick == 'makas' and comp_pick == "taş"):
        result.set("Kazandınız")
    else:
        result.set("Kaybettiniz")

    E1 = Entry(root, font='arial 10 bold', textvariable=resultComputer, bg='antiquewhite2', width=50).place(x=25, y=280)


def reset():
    result.set("")
    user_take.set("")

def Exit():
    root.destroy()


Entry(root, font = 'arial 10 bold', textvariable = result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)

#bilgisayarın Seçimi



root.mainloop()