print('Das Script liest eine mbox-Datei ein und ermittelt die Häufigkeit der E-Mails nach Tageszeit sortiert.')
fname = input('Welche Datei soll verwendet werden? ')
# fname = 'mbox.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

hours = dict()

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        line = line[5].split(':')
        hours[line[0]] = hours.get(line[0],0) + 1

lst = list()

for hour, count in hours.items():
    lst.append( ((hour), (count)) )

lst.sort()

print('Stunde | Anzahl E-Mails')

for item in lst:
    print(item[0],'|',item[1])