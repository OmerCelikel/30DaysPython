
c = {'a' : 10 , 'b': 1 , 'c' : 22}
print(c)
print(c.items())
print(c.values())
print(c.keys())

print(sorted( [ (value , key) for value,key in c.items()]))

d = [ 1, 5 , 2, 3 , 0]
d.sort()
print(d)

css = {'a' : 10 , 'b': 1 , 'c' : 22}
print('\n------------------------------------\n')
mytuple = list()
mytuple2 = list()
for key,value in css.items():
    mytuple.append( (value , key))

for key2,value2 in css.items():
    mytuple2.append( (key2 , value2))

print('Tuple 1: ' , mytuple)
mytuple = sorted(mytuple , reverse=True)
print('Tuple 1: ' , mytuple)

print('Tuple 2: ' , mytuple2)
mytuple2 = sorted(mytuple2 , reverse=True)
print('Tuple 2: ' , mytuple2)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print(days[2])

