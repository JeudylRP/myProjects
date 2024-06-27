'''
-------2. KLASSEN UND OBJEKTEN
---- Klassen
1. Mithilfe der OOP können wir uns eigene Datentypen
definieren, die komplexe Objekte repräsentieren.
 - z.B zur REpresentation eines Autos.
2. Hierzu muss man sich eine entsprechende Klasse definieren.
 - Klasse entpricht Bauplan


---- Eigenschaften:
1. Herstellen (z.B BMW, Mercedes, Tesla)
2. PS-Stärke des Autos
'''
'''
----Was bedeutet "__init__?"
__init__ ist eine spezielle Methode in Python,
die automatisch aufgerufen wird, wenn eine neue 
 Instanz einer Klasse erstellt wird, um diese zu
initialisieren
'''

'''
---- Was ist eine Instanz?
- Eine Instanz ist ein konkretes Objekt das aus einer 
Klasse erstellt wird. Eine Klasse ist wie ein Bauplan,
und eine Instanz ist ein spezifisches Objekt, das
nach diesem Bauplan gebaut wurde. 

- Zum Beispiel:
#########################
class Hund:
   def __init__(self, name):
       self.name = name
mein_hund = Hund(Bello)
#########################
- Hier ist mein_hund eine Instanz der Klasse Hund,
und Bello ist der Name dieses spezifischen Hundes.
'''
'''
---- WICHTIG ZU VERSTEHEN:
Die Klasse  ist der übergreifender Bauplan 
welche wir eben innerhalb unseres Programms beliebig
fest legen können

---- INSTANZEN = KONKRETE OBJEKTE
'''

class Car:
     def __init__(self):
#Kosntruktor: Ist eine spezielle Methode, die beim erstellen
# einer neuen Instanz einer Klasse aufgerufen wird, um
# diese zu Initialisieren.
# In Python ist der Konstruktor die __init__ Methode.
        self.car_brand = None
        self.horse_power = None
        self. color = None


print("Hallo")
car1 = Car()
car1.car_brand = "Audi"
car1.horse_power = 250
car1.color = "blau"
print(car1.car_brand)
print(car1.horse_power)
print(car1.color)


car2 = Car()
car2.car_brand = "BMW"
car2.horse_power = 270
car2.color = "Schwarz"
print(car2.car_brand)
print(car2.horse_power)
print(car2.color)










