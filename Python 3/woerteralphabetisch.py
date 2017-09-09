fhand = open('mail.txt')

woerterbuch = []
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    for word in words:
        woerterbuch.append(word.strip('.?!-,":'))

for word in woerterbuch:
    if word == '':
        woerterbuch.remove(word)

woerterbuch.sort()
ausgabebuch = []

variable = woerterbuch[1]
for word in woerterbuch:
    if word != variable:
        ausgabebuch.append(word)
    variable = word

ausgabebuch.sort()

print(ausgabebuch)