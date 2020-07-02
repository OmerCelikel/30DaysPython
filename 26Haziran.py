# coding=utf-8
"""

# kök bulma
def kökbul(a):
    sonuc = a**(1/2)
    return sonuc


a = int(input("Sayı giriniz"))


sonucum = kökbul(a)

print(sonucum)



tamsSayi = 1                #int
virgulluSayı  = 1.5         #float
karakterDizisi = "ömer"     #string
dogruYanlis = True          #False boolean

# print(tamsSayi + karakterDizisi) Hata Alırız

sayi1, sayi2 , sayi3 , sayi4 = (1,2,3,4)
print (sayi1 , sayi2)

isim = "ömer"
yas = 23


print(isim + " " +  str(yas) + " yasindadır")
cumle = "{a} {b} yasindadır .".format(a = isim, b=yas)
print(cumle)

sayilar = [1 ,2 ,3]

meyveler = ["elma" , "armut" , "karpuz"]

print("sayılar diizm" , sayilar[2])
print(meyveler[0])

sayilar.append(7)
print("sayılar YENİ dizim" , sayilar)

meyveler.sort()

print(meyveler)




# küme
kume = {"elma" , "armut", "karpuz"}
kume.add("kavun")
kume.add("elma")
print (kume)



insan = {
    "ilk isim ": "ömer",
    "soy isim" : "çelikel",
    "yas" : 23
}

print(insan)

print(insan.get('ilk isim') )




# CLASS TANIMLAMA
class Kullanici:
    # constructur method
    def __init__(self , isim , yas):
        self.isim = isim
        self.yas = yas

    def selamla(self):
        print(" ooo . hoşgeldin benim adım {isim}".format(isim = self.isim))

kullanici1 = Kullanici("ömer" , 23)
kullanici2 = Kullanici("ahmet" , 24)
print (kullanici1.isim)
kullanici1.selamla()
kullanici2.selamla()

# Extend
class Musteri(Kullanici):
    def __init__(self , isim , yas):
        self.isim = isim
        self.yas = yas
        self.bakiye = 0
    def bakiyemiSorgula(self):
        return self.bakiye
    def bakiyeArttir(self):
        self.bakiye += 10

msuteri1 = Musteri("ayşe", 2 )

msuteri1.bakiyeArttir()
print (msuteri1.bakiye)
"""