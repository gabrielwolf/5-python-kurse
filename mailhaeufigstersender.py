print('Das Script liest eine mbox-Datei ein und gibt den Absender mit den meisten E-Mails aus.')
fname = input('Welche Datei soll verwendet werden? ')
# fname = 'mbox.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

senders = dict()
maxsender = None
maxsendermails = None

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        senders[line[1]] = senders.get(line[1],0) + 1

for sender in senders:
    if maxsendermails is None or senders.get(sender) > maxsendermails:
        maxsender = sender
        maxsendermails = senders.get(sender)

print(maxsender,maxsendermails)