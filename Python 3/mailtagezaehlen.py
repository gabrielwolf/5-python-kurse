print('Das Script liest eine mbox-Datei ein und ermittelt die Häufigkeit der Wochentage aller Mails.')
fname = input('Welche Datei soll verwendet werden? ')
# fhand = 'mail.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

tage = dict()

print(' ')

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        tage[line[2]] = tage.get(line[2],0) + 1

print(tage)