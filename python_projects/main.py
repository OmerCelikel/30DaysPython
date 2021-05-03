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
root.config(bg='gray8')

#Label oluşturacağız bunu kullanıcı değiştiremeyecek

my_label = Label(root,text ="Taş , Kağıt , Makas" , font='arial 18 bold', bg='orange2').pack()

#Kullanıcı Seçimi , Entry Widget ı input alacak
user_take = StringVar()
user_option = Label(root,text = "Birini seç : taş  kağıt  makas", font='arial 14 bold', bg='orange2').place(x = 65 , y = 70)
Entry(root,font = "arial 15", textvariable = user_take , bg = "orange2").place(x=85 , y = 130)



def computer_choice():
    # burada 3 seçenek var bilgisayarın seçeceği random olarak bilgisayara seçtiriyoruz
    comp_pick = random.randint(1, 3)  # 1 2 3 Taş Kağıt Makas
    if comp_pick == 1:
        comp_pick = 'taş'
    elif comp_pick == 2:
        comp_pick = "kağıt"
    elif comp_pick == 3:
        comp_pick = "makas"
    return comp_pick


#oyunu başlatalım

#sonucu tutuyoruz
#StringVar() = Holds a string; the default value is an empty string ""
result = StringVar()
computer_result= StringVar()

def play():
    user_pick = user_take.get()

    #bilgisayara seçim yaptırdık
    comp_pick = computer_choice()

    print("Bilgisayarın seçimi 2: ", comp_pick)
    print("Benim seçimim : ", user_pick)

    if user_pick == comp_pick:
        result.set("Kazanan yok, berabere")
    elif (user_pick == 'taş' and comp_pick == "makas") or (user_pick == 'kağıt' and comp_pick == "taş") or \
            (user_pick == 'makas' and comp_pick == "taş"):
        result.set("Kazandınız")
    else:
        result.set("Kaybettiniz")

    computer_result.set(comp_pick)


#reset butonu ile sıfırlıyoruz
def reset():
    result.set("")
    user_take.set("")
    computer_result.set("")

def callback():
    print("")

#kapatıyoruz
def Exit():
    root.destroy()



Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='blue2' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='blue2' ,command = reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='blue2' ,command = Exit).place(x=230,y=310)

sonuc = Label(root,text="Username").place(x=40, y=60)
bilgisayar_sonucu = Label(root, text="Password").place(x=40,y=100)

Entry(root, font = 'arial 10 bold', textvariable = result, bg ='orange2',width = 50).place(x=150, y = 250)
Entry(root, font = 'arial 10 bold', textvariable = computer_result, bg ='orange2',width = 50).place(x=150, y = 280)

root.mainloop()