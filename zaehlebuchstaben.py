def countLetters(string, letter):
    return string.count(letter)

string = input('Bitte geben sie einen Text ein: ')
buchstabe = input('Welcher Buchstabe soll gesucht werden? ')
count = countLetters(string, buchstabe)
print('Der Buchstabe',buchstabe,'kommt',count,'x vor.')