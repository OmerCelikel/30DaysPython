# coding=utf-8
# not a -> a yı ters çevir


#PAROLA KONTROLÜ

belirliad = "ömer"
belirlisifre = "1234"
""""
kullanici = input("Kullanıcı Adını Giriniz : ")
sifre = input("Paralanız : ")

if( (belirliad == kullanici) and  (belirlisifre == sifre )  ):
    print("Siteye Giriliyor ... ")
elif((belirliad == kullanici) and (belirlisifre != sifre)):
    print("Şifre Yanlış")
else:
    print("Tekrar Giriniz")

"""
# while (mantık cümlesi):

i = 0

while(i < 10):
    print("i değeri : " , i)
    i +=1
# break - break sonlandırı

while(True):
    kullanici = input("Kullanıcı Adını Giriniz : ")
    sifre = input("Paralanız : ")

    if ((belirliad == kullanici) and (belirlisifre == sifre)):
        print("Siteye Giriliyor ... ")
        break

    elif ((belirliad == kullanici) and (belirlisifre != sifre)):
        print("Şifre Yanlış")
        print ("Şifre Değiştirmek İster Misin   E / H")
        cevap = input()
        if(cevap == "E"):
            yenisifre = input("Yeni Paralo Giriniz : ")
            print("Lütfen Bekleyin...")
            sifre = yenisifre
            print("Şifre Değiştirildi")
        else:
            ("Tekrar Deneyiniz")
            break


    else:
        print ("Tekrar deneyiniz..")


string ="gollum"

#i stringde dolaş
for i in string:
    print(i)
