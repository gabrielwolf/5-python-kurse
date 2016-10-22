fhand = open('lorem.txt','r')

dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        dictionary[word.strip('.?!-,":')] = ''

if 'ipsum' in dictionary:
    print("yeah there's ipsum")

print(dictionary)