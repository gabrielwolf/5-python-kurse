import urllib
import json

while True:
    #address = 'http://python-data.dr-chuck.net/comments_42.json'
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(data)

    countsum = 0
    for comment in info['comments']:
        countsum = countsum + int(comment['count'])
    print 'Sum:',countsum
    break