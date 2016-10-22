#!/usr/local/opt/python3/bin/python3.5
# -*- coding: utf-8 -*-

import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

# ToDo: Deutsche Eingaben mit Komma akzeptieren

print ('Hallo! Mit diesem Script kannst du deinen Lohn berechnen!\n')
print ('Ab der 40. Stunde gibt es 50% Aufschlag.\n')


def warnungAusgeben(text):
    print ('\n\033[91m' + text + '\033[37m\n')


stundensatz = -1  # Eintritt in die Schleife
while stundensatz < 0:
    while True:
        try:
            stundensatz = float(input('Wieviel Euro beträgt dein Stundensatz?\n'))
            break
        except ValueError:
            warnungAusgeben('Bitte den Betrag als Zahl (mit Dezimalpunkt) angeben!')
    if stundensatz < 0:
        warnungAusgeben('Bitte Wert größer 0 angeben!')
    else:
        break

print ('\n')

arbeitszeit = -1  # Eintritt in die Schleife
while arbeitszeit < 0:
    while True:
        try:
            arbeitszeit = float(input('Wieviele Stunden hast du gearbeitet?\n'))
            break
        except ValueError:
            warnungAusgeben('Bitte die Stunden als Zahl (mit Dezimalpunkt) eingeben!')
    if arbeitszeit < 0:
        warnungAusgeben('Bitte Wert größer 0 angeben!')
    else:
        break

def berechneLohn(stundensatz, arbeitszeit):
    # Überstunden mit Faktor 1,5 bewerten
    if arbeitszeit <= 40:
        lohn = stundensatz * arbeitszeit
    else:
        lohn = stundensatz * 40
        ueberstunden = (arbeitszeit - 40) * 1.5
        lohn = lohn + ueberstunden * stundensatz
    return lohn

lohn = berechneLohn(stundensatz, arbeitszeit)
lohn = locale.currency(lohn, grouping=True, international=True)
ausgabe = '\nDu bekommst hoffentlich \033[92m' + lohn + '\033[37m ausgezahlt.'
print (ausgabe)
