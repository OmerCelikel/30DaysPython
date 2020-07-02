# coursera
x = 1 + 2 * 3 - 8 / 4
print(x)

hrs = input("Enter Hours:")
pay = float(hrs) * 2.75
print("Pay: ",pay)

# --------------------------------------

astr = "Hello Ömer"

try:
    istr = int(astr)
except:
    istr = -1

print ("İlki :", istr)


astr = "123"

try:
    istr = int(astr)
except:
    istr = -1

print ("İkincisi: " , istr)


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print("ister: ",istr)
x =6
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')