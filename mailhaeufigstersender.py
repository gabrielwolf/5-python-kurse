print('Das Script liest eine mbox-Datei ein und gibt den Absender mit den meisten E-Mails aus.')
fname = input('Welche Datei soll verwendet werden? ')
# fname = 'mbox.txt'
try:
    fhand = open(fname,'r+')
except:
    print('Datei konnte nicht geöffnet werden:', fname)
    exit()

senders = dict()

for line in fhand:
    if line.startswith('From '):
        line = line.split()
        senders[line[1]] = senders.get(line[1],0) + 1

# Dictionary in Liste aus Tupeln kopieren um leicht nach der größten Anzahl an Mails sortieren zu können
lst = list()

for email, count in senders.items():
    lst.append( ((count), (email)) )

lst.sort(reverse=True)
count, email = lst[0]

#Ausgabe
print(email, count)