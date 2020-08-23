import socket

mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#               HOST                PORT
mysock.connect( ('data.pr4e.org' , 80) )
print(mysock)

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n' .encode()
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    #print('SA')
mysock.close()

print('\n------------------------------\n')

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

print('\n------------------------------\n')

fhand1 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line1 in fhand1:

    words = line1.decode().split()
    print('words : ', words)
    for word in words:
        counts[word] = counts.get(word, 0) +1
print(counts)

print('\n------------------------------\n')

fhand2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')

for line2 in fhand2:
    print(line2.decode().strip)

