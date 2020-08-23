"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
eachHour = []
for line in handle:
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split()
    if len(words)> 3:
        myTime = words[5]

        bigTime = myTime.split(':')
        myBigtime = bigTime[0]
        eachHour.append(myBigtime)


counts = dict()
for x in eachHour:

    counts[x] = counts.get(x , 0) + 1


myTuple = list()
for key , value in counts.items():
    myTuple.append( (key , value) )

myTuple = sorted(myTuple , reverse = True)


mynumber = len(counts.items())


while mynumber > -1:
    mynumber-=1
    if mynumber == 0:
        break

for val,key in myTuple[ : : -1] :
    print(val,key)


04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1


"""