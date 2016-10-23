from operator import itemgetter

fhand = open('lorem.txt','r')

dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        word = word.strip('.?!-,":()0123456789')
        word = word.lower()
        dictionary[word] = dictionary.get(word,0) + 1

# Dictionary in Liste kopieren
lst = list(dictionary.keys())
# print('Debug:',lst)
for i in range(len(lst)):
    lst[i] = [dictionary[lst[i]], lst[i]]

# Nach Häufigkeit sortieren
lst.sort(key=itemgetter(0), reverse=True)

# Ausgabe
for item in lst:
    print(item[0],item[1])