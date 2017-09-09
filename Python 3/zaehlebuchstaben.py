import string

print('Häufigkeit von Buchstaben eines Textes.')
fname = input('Welche Datei soll verwendet werden? ')
#fname = 'mbox.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

file = fhand.read()

file = file.lower()                   # nur Kleinbuchstaben
file = file.replace(' ', '')          # keine Leerzeichen
file = file.replace('\n', '')         # keine Zeilensprünge
file = file.replace('\t', '')         # keine Tabulaturzeichen

i = 0
while i < 10:                         # keine Zahlen
    file = file.replace(str(i), '')
    i = i + 1

punctuation = string.punctuation      # keine Interpunktion
for letter in punctuation:
    file = file.replace(letter, '')

dictionary = dict()

for letter in file:
    dictionary[letter] = dictionary.get(letter,0) + 1

lst = list()

for buchstabe, count in dictionary.items():
    lst.append( ((count), (buchstabe)) )

lst.sort(reverse=True)

for buchstabe in lst:
    print(buchstabe[1], buchstabe[0])
