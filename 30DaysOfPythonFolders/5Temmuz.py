# coding=utf-8

"""


print("1. SORU - Bir Aydaki Gün Sayısı")
print (" ")
from calendar import monthrange
aylar = ["ocak" ,"şubat","mart","nisan","mayıs","haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]

ayIsim = input("Gün Sayısını öğrenmek istediğiniz ay isimini giriniz :")

# girilen ay listede aranacak
# ay numarasına göre kaç gün olduğu bastırılacak
sayac = 1 # ay numarasu
for i in aylar:
    if ayIsim ==i:
        ayIsim = ayIsim.capitalize() #ay ı büyük harf yapıldı
        sayac = monthrange(2020, sayac)[1]  # monthrange ( yıl , ay ) alınır
        print ("2020 yılındaki", ayIsim, "Ayı", sayac, "gündür")
        if ayIsim == "Şubat":
            print("Bazen 28 gün de olabilir")


    sayac = sayac +1 # ay numarası arttırıllıyor

print (" ")

# -----------------------------------
print("2. SORU - Richter Ölçeği")
print (" ")

buyukluk = float(input("Deprem büyüklüğünü giriniz: "))

tanımlayıcı = ["Mikro", "Çok Küçük", "Küçük", "Hafif", "Orta", "Şiddetli", "Çok Şiddetli" , "Çok Çok Şiddetli","Meteor"]

# ilk Mikro değerimiz iki aralıkta olduğundan if e
# son 10 dan büyükleri de belli etmek için elif e alındı
# diğer aralıklarımız aradaki değerler olacağından

if buyukluk > 0 and buyukluk < 2 :
    print(buyukluk,"büyüklüğündeki deprem" ,tanımlayıcı[0] , "boyutta depremdir")
elif buyukluk > 10:
    print(buyukluk, "büyüklüğündeki deprem", tanımlayıcı[8], "boyutta depremdir")
else:
    print(buyukluk, "büyüklüğündeki deprem", tanımlayıcı[int(buyukluk) - 1], "boyutta depremdir")



print (" ")
# -----------------------------------
print("3. SORU - Boşluk olana kadar Meyve ekleme ve bastırma")
print (" ")

# girilenleri kümeye koyacağız
# küme bastırılınca içindeki tekrarlıları basmaz
küme = set()
while True:
    meyve = input("Kelime Giriniz: ")
    if meyve == " ":
        break
    küme.add(meyve) # kümeye meyve ekleme

print ("Girilen Kelime Listesi" , küme)

print (" ")

# -----------------------------------
print("4. SORU - String Değer Sayısal")

# bulduğumuz değerleri en son bastırmak için boş bir liste
bosliste = []
value = [" ",
         ["." , "," , "?", ":" ,";","!"],
         ["A","B","C","Ç"],
         ["D","E","F"],
         ["G","Ğ","H","I"],
         ["İ","J","K","L"],
         ["M","N","O","Ö"],
         ["P","R","S"],
         ["Ş","T","U","Ü"],
         ["V","Y","Z"]
         ]

for i in value:
    print (i)

metin = input("Metin giriniz: ")

metin = metin.upper() # value ler büyük olarak ayarlandı
#print (metin)

# iç içe döngü kullanılacak
#girilen metni harf harf tarayacağız
metinsayac = 0

# girilen metinin ilk harfinden başlanılarak bakılacak
# eğer metindeki karf, value değerlerimizden birine eşitse onu alacak
for harftutma in metin:
    keycounter = 0
    for i in value:
        # değerin kaçıncı sırada olduğunu almak için, 3 kere 7 bastırmak için 777
        count = 1

        #tüm valueleri görmek ve eşleşen varsa bulmak için
        for j in i:
            if (metin[metinsayac] == j):
                #print ("eşleşen harf var , ", j, " ve ", metin[metinsayac] , "Count : " , count,"keycouner  : " , keycounter)
                #print (count * str(keycounter))
                gösterilecekDegerler =  count * str(keycounter)
                #boş listemize gösterilecel değerleri ekliyoruz
                bosliste.append(gösterilecekDegerler)
            count = count + 1

        keycounter = keycounter + 1

    metinsayac = metinsayac + 1 #girilen metindeki harflere teker teekr bakılıyor


print ("Girilen Metnin Karşılığı : " ,bosliste)

print (" ")
# -----------------------------------
"""
print("5. SORU - Vücut Kitle İndeksi (csv ekleyerek)")
print (" ")

