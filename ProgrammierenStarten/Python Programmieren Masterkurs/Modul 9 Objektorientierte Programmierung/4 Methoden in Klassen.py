'''
------- 4. METHODEN IN KLASSEN
---- Was haben wir gelernt?
1. Prinzip der Objektorientierten PROGRAMMIERUNG
- Komplexe Objekte aus der realen Welt innerhalb
unserer Programme nachmodellieren
2. Definition von Klassen
3. Definition der Attribute innerhalb des Konstruktors
4. Klassen stellen lediglich innerhalb des Konstruktors
5. Klassen stellen lediglich den Bauplan dar
- Für konkretes Arbeiten mit diesen müssen zunächst Objekte
instanziiert werden.
6. Mit dem Punkt-Operator kann auf spezifishce Attribute
der Objekte zugegriffen werden.

---- Klassendefinition um Methoden zu erweitern
1. Bisher besitzt unsere Klasse "Car" nur Attribute (Eigenschaften)
2. Klasse verfügt bisher nicht über Funktionalität
- z.B. kann das Auto aktuell noch nicht fahren, da es keine
Funktionalität hierfür besitzt.
3. Lösung: Methoden
- Funktionen, die innerhalb einer Klasse definiert werden und deshalb
auch nur von Objekten dieser Klasse verwendet werden können
'''


class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.xPosition = 5
        self.yPosition = 5

    def drive(self, x, y):
        # Self benutz man um Objekte zu referenzieren
        self.xPosition += x
        self.yPosition += y

    def print_position(self):
        print("Aktuelle Position des Autos: x="
              +str(self.xPosition) +" | y="+ str(self.yPosition))


print("Hello")
car1 = Car()
car1.car_brand = "Audi"
car1.horse_power = 250
car1.color = "blau"
print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car1.print_position()
car1.drive(5,10)
car1.print_position()



car2 = Car()
car2.car_brand = "BMW"
car2.horse_power = 270
car2.color = "Schwarz"
print(car2.car_brand)
print(car2.horse_power)
print(car2.color)

car3 = car1
car3.horse_power = 100

print(car1.horse_power)
print(car2.horse_power)
print(car3.horse_power)











