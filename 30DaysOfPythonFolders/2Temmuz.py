hrs = input("Enter Hours:")
h = float(hrs)

if h<40:
    pay = h*10.5
    print("Your pay:",pay)
else:
    pay = 40*10.5 + (h-45)*(10.5*1.5)
    print(pay)

# DEF

def thing():
    print("Hello functions")


thing()
