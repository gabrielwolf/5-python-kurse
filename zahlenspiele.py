#!/usr/bin/python
# -*- coding: utf-8 -*-

print('Spiel mit Zahlen.')

def warnungAusgeben(text):
    print ('\n\033[91m' + text + '\033[37m\n')

eingabe = 0
zahlen = []
while eingabe != 'ende':
    while True:
        eingabe = input('Bitte geben sie eine Zahl oder "ende" ein: ')
        try:
            zahl = float(eingabe)
            zahlen.append(zahl)
            break
        except ValueError:
            if eingabe == 'ende':
                break
            else:
                warnungAusgeben('Fehler! Bitte Zahl eingeben: ')

anzahl = len(zahlen)
summe = 0
for zahl in zahlen:
    summe = summe + zahl
mittelwert = summe / anzahl

print('Anzahl an Zahlen:', anzahl)
print('Summe:', summe)
print('Mittelwert:', mittelwert)
