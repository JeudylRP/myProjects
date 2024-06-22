'''
------ Die if-Anweisung in Kombination mit dem else-Zweig.
'''

number = int(input("Bitte gebe eine Ganzzahl ein: "))

if number <10:
    print("Die eingegebene Zahl ist kleiner als 10 ....")
    print("Das ist ein Test")
    number = True
else:
    print("Die eingegebene Zahl ist 10 oder grösser als 10")

    print("Hier gehts weiter")