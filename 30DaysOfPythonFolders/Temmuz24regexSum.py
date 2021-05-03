
import re

hand =  open('regex_sum_42.txt') #http://py4e-data.dr-chuck.net/regex_sum_740388.txt
#to put my all numbers
numberArr = []
for line in hand:
    line = line.rstrip()
    #look each line and find numbers
    numbers = re.findall('[0-9]+',line)

    #some of lines don't have any numbers
    if not numbers: continue
    #add these numbers to my arrayList
    numberArr.append(numbers)
#print(numberArr)

mySum = 0
#NumberArr List is a Multiple dimensional ArrayList

for x in numberArr:
    for y in x:
        #print(type(y)) _-> y is str, converting the extracted strings to integers
        nowInteger = int(y)
        #print(nowInteger)
        mySum += nowInteger

print('My Sum : ',mySum)