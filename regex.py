import re

print('Das Script sucht alle Textvorkommnisse à la `New Revision: 123456` und gibt den Durchschnitt aller vorkommender Zahlen aus')

fhand = open('mbox.txt')

match = []

r = 'New.+:.([0-9]+)'

for line in fhand:
    pattern = re.findall(r, line)
    if pattern != []:
        match.append(pattern)

summe = 0

for item in match:
    summe = summe + float(str((item[0])))

print(summe)