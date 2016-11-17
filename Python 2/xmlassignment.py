import urllib
import xml.etree.ElementTree as ET

while True:
    #address = 'http://python-data.dr-chuck.net/comments_42.xml'
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print 'Count:',len(counts)

    countsum = 0
    for i in range(len(counts)):
        countsum = countsum + int(counts[i].text)
    print 'Sum:',countsum
    break