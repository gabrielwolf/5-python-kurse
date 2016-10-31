import re

print('Das Script gibt alle Zeilen der mbox-Datei aus, die dem Regulären Ausdruck entsprechen')

fhand = open('mbox.txt')

r = ''
r = input('Gib einen regulären Ausdruck ein: ')
counter = 0

for line in fhand:
    match = re.findall(r, line)
    if match != []:
        counter = counter + 1

print('mbox.txt hat',counter,'Zeilen die',r,'enthalten.')