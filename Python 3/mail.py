print('Das Script liest eine mbox-Datei ein und gibt die enthaltenen Senderadressen aus.')
fname = input('Welche Datei soll verwendet werden? ')
# fhand = 'mail.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

senders = dict()

print(' ')

for line in fhand:
    if line.startswith('From'):
        line = line.split()
        senders[line[1]] = senders.get(line[1],0) + 1

print('Absender:',senders)
print('\nDie Datei enthält',len(senders),'Absenderadressen.')