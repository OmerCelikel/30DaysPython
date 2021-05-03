# Dictirionaries

purse = dict()

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

# whats in purse
print(purse)
# {'money': 12, 'candy': 3, 'tissues': 75}

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
purse['candy'] += 2
print(purse)

lst = list()
lst.append(12)
print("lst : " , lst)

lst2 = []
lst2.append(13)
print("lst2: " ,lst2)

kisiler = {'Ömer':22, 'Gökçe' : 23, 'besra': 17}
print(kisiler)

print('\n---------------------\n')

ccc = dict()
print(ccc)
#print(ccc['varmı'])
KeyError = 'varmı'
print('varmı' in ccc)
print('\n---------------------\n')

counts = dict()
names = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

print('\n---------------------\n')

counts2 = dict()
names2 = ['csev' , 'cwen' , 'csev' , 'zqian' , 'cwen']
for name2 in names2:
    counts2[name2] = counts2.get(name2 , 0) + 1
print(counts2)

print('\n---------------------\n')
counts3 = dict()
print('Enter a line or text: ')
line = input(' ')
words = line.split()

print('words : ',words)

print('Counting...')

for word in words:
    counts3[word] = counts3.get(word,0) + 1
print('Counts',counts3)

print('\n---------------------\n')

counts4 = {'naber': 100 , 'nasılsın' : 2 , 'keyifler' : 3}

for key in counts4:
    print(key , counts4[key])
    print('key : ',key)
    #print('counts: ' , counts4)
    print('Counts[key]: ' , counts4[key])
    print()
print('\n---------------------\n')

print(list(counts4))
print(counts4.keys())
print(counts4.values())
print(counts4.items())

for key,value in counts4.items():
    print(key,value)

stuff = dict()
print(stuff.get('candy', -1))


"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = []
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    word = line.split()
    emails = word[1]
    #print(emails)
    words.append(emails)
#print(words)

counts = dict()

for x in words:
        counts[x] = counts.get(x , 0) + 1
        
#print(counts)
        
values = None
mycount = None

for word,count in counts.items():
    if mycount is None  or (count > mycount):
        values = word
        mycount = count
print(values,mycount)
"""
print('\n---------------------\n')

# tuples

d = {'a': 10 , 'c' : 22, 'b' : 1}
print(d.items())

print(sorted(d.items()))

