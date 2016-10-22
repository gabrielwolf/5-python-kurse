print('Dieses Script gibt nach der Eingabe von Zahlen die Größte und Kleinste aus.')

def warnungAusgeben(text):
    print ('\n\033[91m' + text + '\033[37m\n')

zahlen = []
eingabe = ''

while eingabe != 'ende':
    while True:
        eingabe = input('Bitte geben sie eine Zahl ein. Zum Beenden schreiben sie "ende": ')
        try:
            zahl = float(eingabe)
            zahlen.append(zahl)
            break
        except ValueError:
            if eingabe == 'ende':
                break
            else:
                warnungAusgeben('Fehler! Bitte Zahl eingeben (z.B. 3, 34.2, -3)')

print('Die Größte Zahl ist:',max(zahlen),'\nDie Kleinste:',min(zahlen))