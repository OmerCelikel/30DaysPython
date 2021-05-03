print("hellooo")
print ("çalıştş")
print(5+6)
x = "ömer"
y = "çelikel"

print("Ad : " + x  )
print( "Soyad : " + y)

print(len(x))
print (str(3))
print(int("6") + 8)


z = [1,2,"ömer",22,2.4]
print(z)
z[2] = 3
print(z)
z.append("selam")
print(z)


a = input("Birinci sayıyı giriniz : ")

b = input("ikinci sayıyı giriniz : ")

z = int(a)+int(b)
print(z)
#  print te integer ı kabul etmedi str yaparak z yi bastım

print ("Toplamlar : " + str(z))
print("--------------------------------------------")

print("oyuncu kaydetme")

ad = input("Oyuncu adı giriniz : ")
soyad = input("Soyad giriniz : ")

takım = input("Takım Giriniz : ")

bilgiler = [ad,soyad,takım]

print("Kaydediliyor...")

print("Oyuncu ad : " , ad , "Soyadı : " , soyad , "Takım : " , takım)

print("kaydedildi....")

print("--------------------------------------------")

# if else

yas = int(input("Yaşınızı giriniz"))

if yas >=18:
    print ("Mekana girebilirsin")
else:
    print("Yaşınız yetmiyor")
    gerekli = 18 - yas
    print(gerekli , " yıl sonra girebilirsiniz ")


note = int(input("Notunuz"))
# == !=     >    >=    <=
if note > 90:
    print("A")
elif note > 70:
    print("B")
else:
    print("kaldınız")
# if else bittti 9, video bitti