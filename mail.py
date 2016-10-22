print('Das Script liest eine mbox-Datei ein und gibt die enthaltenen Senderadressen aus.')
file = input('Welche Datei soll verwendet werden? ')
# file = 'mail.txt'
file = open(file,'r+')

senders = dict()

print(' ')

for line in file:
    if line == '':
        line.remove()
    elif line[0:4] == 'From':
        line = line.split()
        senders[line[1]] = senders.get(line[1],0) + 1

print('Absender:',senders)
print('\nDie Datei enthält',len(senders),'Absenderadressen.')