fhand = open('lorem.txt','r')

dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        word = word.strip('.?!-,":()0123456789')
        word = word.lower()
        dictionary[word] = dictionary.get(word,0) + 1

# Dictionary in Liste kopieren
lst = list()

for key, val in list(dictionary.items()):
    lst.append( (val, key) )

# Nach Häufigkeit sortieren
lst.sort(reverse=True)

# Ausgabe
for key, val in lst[:100]:
    print(key, val)