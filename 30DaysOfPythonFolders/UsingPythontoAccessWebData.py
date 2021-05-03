print('Let \'s start to the course' )

hand =  open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)

print('\n ------------------------------- \n')
# It is equals to this

#import regular expression

import  re

hand1 = open('mbox-short.txt')
for line1 in hand1:
    line1 = line1.rstrip()
    #re search = startswith -> ^ Cümlenin başına bakar
    if re.search('^From:',line1):
        print(line1)
    if re.search('^X-'
                 ''
                 ''
                 '', line1):
        print('GArip')
        print(line1)

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
y11 = re.findall('[a-z0-9]+',x)
y1 = re.findall('[a-z]+',x)

print('y:',y)
print('y1:',y1)
print('y11:',y11)

x2 = 'From: Using the: character'
y2 = re.findall('^F.+',x2)
y3 = re.findall('^F.+:',x2) # artıdan sonragi string en son biten stringdir.
print('y2:',y2)
print('y3:',y3)
y4 = re.findall('^F.+?:',x2) # artıve soru işsrt sonragi string ilk
print('y4:',y4)


print('\n ------------------------------- \n')

mysentence = 'From stephne.marq@uct.ac.za Sat Jan5 09:14:16 2008'
email= re.findall('\S+@\S+', mysentence)
print(email)

email2= re.findall('^From (\S+@\S+)', mysentence)
print(email2)

whereFrom = re.findall('@([^ ]*)' , mysentence)
print(whereFrom)

whereFrom2 = re.findall('^From .*@([^ ]*)',mysentence)
print('whereFrom2 : ',whereFrom2)