print('Das Script liest eine mbox-Datei ein und gibt alle Domains der Absenderadressen mit Häufigkeit aus.')
fname = input('Welche Datei soll verwendet werden? ')
# fname = 'mbox.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

mailadressen = dict()

print(' ')

for line in fhand:
    if line.startswith('From '):
        line = line.split('@')
        line = line[1].split()
        domain = line[0]
        mailadressen[domain] = mailadressen.get(domain,0) + 1

print(mailadressen)