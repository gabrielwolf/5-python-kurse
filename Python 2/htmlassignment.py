import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

temptags = soup('a')
print 'Retrieving:',url

i = 1
while i <= count:
    tempurl = temptags[position-1].get('href', None)
    print 'Retrieving:',tempurl
    temphtml = urllib.urlopen(tempurl).read()
    tempsoup = BeautifulSoup(temphtml)
    temptags = tempsoup('a')
    i = i + 1