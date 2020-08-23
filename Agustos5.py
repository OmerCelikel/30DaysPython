# urllib eklenmeli
#açılan linkteki sayılar toplandı
import urllib.request , urllib.parse , urllib.error
#beautiful soup
from bs4 import BeautifulSoup

#güvenli siteler için https
import  ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# http://py4e-data.dr-chuck.net/comments_42.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
mySum = []
count = 0
# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    #print('Contents:', tag.contents[0])
    myNumer = tag.contents[0]
    mySum.append(int(myNumer))
    count +=1
print('Count',count)
print('Sum',sum(mySum))

