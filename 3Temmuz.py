# coding=utf-8
"""
def computepay(h,r):
    if h<=40:
    	p = h*r
    else:
    	p = 40*r + (h-40)*(r*1.5)

    return p

hrs = input("Enter Hours:")
h = int(hrs)
ratem = input("Enter Rate:")
r = float(ratem)

p = computepay(h,r)
print("Pay",p)

"""

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        mynum = int(num)
    except:
        print("Invalid input")
        continue
        # to find smallest
    if smallest is None:
        smallest = mynum
    elif smallest > mynum:
        smallest = mynum
    # to find largest

    if largest is None:
        largest = mynum
    elif largest < mynum:
        largest = mynum


print("Maximum is", largest)
print("Minimum is",smallest)

"""
    if mynum > largest:
        largest = mynum
    else:
        print ("largest çalışmadı")

    if smallest > mynum:
        smallest = mynum

    print(largest, " ", smallest)

"""