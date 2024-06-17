'''
----- Mathoden in Klassen
'''

'''
----- Arten von Speicherplätze:
-1. Primärspeicher (Hauptspeicher).
-2. Sekundärspeicher.
-3. Tertiärspeicher.
-4.Virtueller Speicher.
-5.Spezial-Speicher.


----- Wa sind Methoden?
In der Programmierung sind Methoden Funktionen, die an Objekte gebunden sind und 
auf die Daten dieser Objekte zugreifen und diese manipulieren können.

Sie sind ein Bestandteil der OOP ubd ermöglichen es, da Verhalten und die Zuständ von Objekten 
zu dfinieren und zu steuern.

----- Was sind Konstruktoren?
Ein Kosntruktor ist eine spezielle Funktion in der Programmierung,
die automatisch aufgerufen wird,
wenn du ein neues Objekt von einer bestimmten Art (einer Klasse) 
erstellst.
!!!!-> Der Zweck des Konstruktors besteht darin, dieses neue Objekt
vorzubereiten und initialisieren.

------ Was bedeutet "__init__-Methode?

Die__init__-Methode in Python ist eine spezielle Methode, die
als Konstruktor dient. Sie wird automatisch aufgerufen, wenn eine neue 
Instanz (Ein Objekt) einer Klasse erstellt wird. 
!!!!-> Ihre Hauptaufgabe ist es, das neue erstellete Objekt zu initialisieren,
indem sie dessen Attribute mit Werten versieht und eventuell notwendige 
Startkonfigurationen vornimmt.




'''


class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.y_position = 5

    def drive(self, x, y):
        self.x_position += x
        self.y_position += y

# Die Koordinaten als Attribut definieren!!

car1 = Car()
print(car1.x_position)  # Ausgabe: 5
print(car1.y_position)  # Ausgabe: 5
car1.drive(5, 10)
print(car1.x_position)  # Ausgabe: 10
print(car1.y_position)  # Ausgabe: 15

