import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_323515.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Get interesting values
tags = soup('span')

# We want the sum
total = 0
for tag in tags:
    total = total + int(tag.contents[0])

print 'Count',len(tags)
print 'Sum',total