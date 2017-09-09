import re

print('Das Script gibt alle Zeilen der mbox-Datei aus, die dem Regulären Ausdruck entsprechen')

fhand = open('mbox.txt')

r = ''
r = input('Gib einen regulären Ausdruck ein: ')
counter = 0
match = None

for line in fhand:
    try:
        match = re.findall(r, line)
    except re.error:
        print('Leider kein korrekter regulärer Ausdruck.')
        r = input('Gib einen regulären Ausdruck (Python) ein: ')
    if match != []:
        counter = counter + 1

print('mbox.txt hat',counter,'Zeilen die',r,'enthalten.')