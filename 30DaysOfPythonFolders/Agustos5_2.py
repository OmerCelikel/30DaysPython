# urllib eklenmeli
#Linkten linge giden bir çalışma yapıldı
import urllib.request , urllib.parse , urllib.error
#beautiful soup
from bs4 import BeautifulSoup

#güvenli siteler için https
import  ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position=int(position)

url = input('Enter - ')
""" To put my Links """
myLinks = []
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
sayac = 0
while sayac < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        # print(tags)
        #print('genel ', tag.get('href', None))
        myLinks.append(tag.get('href', None))

    url = myLinks[position - 1]
    myLinks = []
    print('Retriving:', url)
    sayac += 1