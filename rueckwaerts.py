print('Dieses Programm spuckt deine Eingabe rückwärts aus!')

def rueckwaerts(string):
    return string[::-1]

eingabe = input('Was möchtest du rückwärts ausgeben? ')
ausgabe = rueckwaerts(eingabe).title()
print(ausgabe)