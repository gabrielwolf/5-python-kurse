print('Das Script liest eine mbox-Datei ein und gibt die enthaltenen Senderadressen aus.')
file = input('Welche Datei soll verwendet werden? ')
# file = 'mail.txt'
file = open(file,'r+')

senders = []

print(' ')

for line in file:
    if line == '':
        line.remove()
    elif line[0:4] == 'From':
        line = line.split()
        senders.append(line[1])
        print(line[1])

print('\nDie Datei enthält',len(senders),'Senderadressen.')