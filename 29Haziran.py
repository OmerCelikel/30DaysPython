# coding=utf-8
# kullanıcı parametreye bir şery girmediğinde belli olanlar gelecek
def kayit_ekle(ad ="bilgi yok",soyad="bilgi yok",yas = "Bilgi yok" ,meslek ="bilgi yok"):
    print("kayıt ekleniyor")

    print("Adı: {}\n Soyad: {}\n Yaş: {}\n Meslek: {}\n ".format(ad,soyad,yas,meslek) )
    print("kayıt Başarıyla eklendi")

# sirali girmeliyiz
# kayit_ekle("Ömer","Çelikel")
kayit_ekle("Ömer", yas=23)

# ---------------------------------------------------------------
# RECURSION

def topla(liste):
    if(len(liste)) == 0:
        return 0
    else:
        return liste[0] + topla(liste[1:])

sonuc = topla([1,2,3,4,5,6])

print(sonuc)
# ---------------------------------------------------------------
# global ve yerel degisken

a = 10

def fonksiyon():
    #global a
    a = 2
    print(a)
fonksiyon()
print(a)
# ---------------------------------------------------------------
# dictionary

sozluk = {"Python" : "Guzel bir dil" , "Java" : "Onceki ogrendigim"}

print (type(sozluk))

print(sozluk["Python"]) # bana "Guzel bir dil YAZDIRACAK

for i in sozluk.items():
    print (i)

for i in sozluk:
    print("İkinci print" , i)