print('Hier kannst du die Fakultät ausrechnen.')

fakultaet = float(input('Welche Fakultät willst du berechnen?'))

durchgang = 1.0
ergebnis = 1.0
while durchgang <= fakultaet:
    ergebnis = ergebnis * durchgang
    durchgang = durchgang + 1

print(ergebnis)