'''
import urllib.request
import json

url = input("Enter URL: ")

#response = urllib.request.urlopen(urllib.request.Request(url)).read().decode('utf-8')
myRequest = urllib.request.Request(url)
response = urllib.request.urlopen(myRequest)
responseRead = response.read()
decoding = responseRead.decode()
print(decoding)
data = json.loads(decoding)
counts = list()

comments = data['comments']
for comment in comments:
    counts.append(comment['count'])

print (sum(counts))

'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
print('Retrieving', url)


uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode() #decode() alt alta güzel şekilde gösterim
print('Retrieved', len(data), 'characters')
print(data)
#print('\n ========================================== \n')

info = json.loads(data) # datayı (arrrayi) json a ekleme yapıyor

#print(info)
#print(info) #to see the info dictionary/object
#print('\n ========================================== \n')
#print(json.dumps(info, indent=2))  # is equal to  print(data)

myCount = 0
mySum = 0

for item in info['comments']:
    num = item['count']
    mySum = mySum + int(num)
    myCount = myCount + 1

print('Count: ', myCount)
print('Sum: ', mySum)