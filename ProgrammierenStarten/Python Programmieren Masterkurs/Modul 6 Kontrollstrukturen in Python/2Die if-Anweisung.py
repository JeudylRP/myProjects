'''
------ Die if-Anweisung -----
casten int(input(...))
'''

number = int(input("Bitte gebe eine Ganzzahl ein: "))

if number < 10:
    print("Die eingegebene Zahl ist kleiner als 10...")
    print("Das ist ein Test")
    number = True
print(number)
print("Hier gehts weiter")