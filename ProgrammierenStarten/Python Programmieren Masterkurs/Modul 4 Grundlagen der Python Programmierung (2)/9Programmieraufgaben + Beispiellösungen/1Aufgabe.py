'''
------ AUFGABE 1:
In dieser Aufgabe gilt ein Programm zu
schreiben, mit welchem du Personen erfassen
kansst. Hierzu soll zunächst der Vorname des
Nutzers abgefragt und eingelesen werden, Daraufhin
sollen dann im Anschluss auch noch der Nachname
und das Alter des Nutzers abgefragt und eingelesen
werden. Sobald alle drei Werte eingelesen wurden,
soll der komplette Name samt Alter übersichtlich auf
der Konsole ausgegeben werden.


vorname = input("Wie ist dein Vorname? ")
nachname = input("Wie ist dein Familienname? ")
age = input("Wie alt bist du? ")

print("Dein Name lautet: "+vorname+" "
      +nachname+ " und du bist "+age+" Jahre alt")
'''

first_name = input("Bitte Vornamen eingeben: ")
last_name = input("Bitte Nachnamen eingeben: ")
age = int(input("Bitte das Alter eingeben: "))

print(first_name + " " + last_name + " ist "
+ str(age) + " Jahre alt.")


