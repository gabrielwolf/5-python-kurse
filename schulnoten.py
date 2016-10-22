#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

print ('''
Hallo! Mit diesem Script kannst du aus deiner Note (0.0 bis 1.0)
den englischen Grade (A, B, C, D, F) berechnen!
''')


def warnungAusgeben(text):
    print ('\n\033[91m' + text + '\033[37m\n')


note = 0  # Eintritt in die Schleife
while note >= 0 or note <= 1:
    while True:
        try:
            note = float(input('Welchen Wert hat dein Note? (z.B. 0.4 oder 1.0)\n'))
            break
        except ValueError:
            warnungAusgeben('Bitte den Wert als Zahl (mit Dezimalpunkt) angeben!')
    if note < 0 or note > 1:
        warnungAusgeben('Bitte Wert zwischen 0 und 1 angeben!')
    else:
        break

print ('\n')

if note >= 0.9:
    grade = 'A'
elif note >= 0.8:
    grade = 'B'
elif note >= 0.7:
    grade = 'C'
elif note >= 0.6:
    grade = 'D'
elif note < 0.6:
    grade = 'F'

ausgabe = 'Du hast einen \033[92m' + grade + '\033[37m Grade.'
print (ausgabe)
