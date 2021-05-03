# coding=utf-8
# faktöriyel bulma

faktoriyel = 1
while True:
    sayi = int(input("Sayı Giriniz : "))

    for i in range(1 , sayi+1):

        faktoriyel *= i
    print (sayi ,". Faktöriyeli : ", faktoriyel)
    break

# FONKSİYONLAR

def merhaba(a):
    print("Merhaba Fonksiyonu Çalıştırıldı")
    print(a+2)

merhaba(2)

def faktoriyelFonk(sayi2):
    faktoriyel2 = 1
    for i in range(1, sayi2 + 1):
        faktoriyel2 *= i
    #print (sayi2, ". Faktöriyeli : ", faktoriyel)
    #print yerine return ile aktaracağım
    return faktoriyel2

sayi2 = int(input("Sayı Giriniz"))

faktoriyelFonk(sayi2)
print("PRint fonksiyon")
fonskiyondanGelen = faktoriyelFonk(sayi2)
print(fonskiyondanGelen)