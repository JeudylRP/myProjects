'''
------- 5. MÖGLICHKEITEN DES KONTRUKTORS:
---- Unterschied zwischen Explizit und Implizit
1. In der Programmierung beziehen sich die Begriffe
"explizit" und "implizit" auf die Art und Weise, wie
bestimmte Aktionen oder Aussagen ausgedrückt und verstanden
werden.
-- Hier sind die Definitionen und Beispiele für beise Begriffe:

---EXPLIZIT---
1. Explzit bedeutet, dass etwas klar und deutlich ausgedrückt
oder angegeben ist.
In Python bezieht sich explizite Programmierung darauf,
dass der Code deutlich beschreibt, was er tut. Dies folgt dem
Prinzip "Explizit ist better tan implicit" aus dem Zen of Python.

---- Beispiele für explizite Programmierung: ----
1. variable Declaration:
########################
counter = 0
########################
2. Klare Funktion und Variablennamen:
#########################
def calculate_area(radius):
    return 3.14 *radius * radius
#########################
3. Explizite Typumwandlunng:
#########################
user_input = "42"
user_age = int(user_input)
#########################

---IMPLIZIT---
1. Implizit bedeutet, dass etwas nicht direkt ausgedückt,
sondern aus dem Kontext oder der Konvention abgeleitet wird.
In Python bedeutet dies, dass bestimmte Aktionen oder Interpretationen
autamatisch und ohne explizite Anweisungen geschehen.

--- Beispiele für impizite Programmierung:
1. Typinferez in Schleifen:
########################
for i in range (10):
   print(i)
########################
2. Automatishe Typumwandlung
########################
result = 5 + 3.0
# Die 5 wird implizit in einen Float umgewandelt, um das
Erbegnis 8.0 zu erhalten
########################
3. Implizite Rückgabewerte in Funktionen ohne Return-Aussage:
########################
def do_nothing():
pass # Diese Funktion gibt implizit None zurück
########################

--- Zusammenfassung ---
1. Explizit: Klar und deutlich im Code angeben.
Beispiel: int("42") um eine Zeichenkette in eine Ganzzahl
zu konvertieren.

2. Implizit: Automatich oder aus dem Kontext abgeleitet.
Beispiel: Automatische Typumwandlung 5 + 3.0.

Wichtig!!! ---> In der Python Programmierung wird oft empfolen,
explizit zu sein, da dies den code lesbarer und wartbarer macht.

'''


class Car:
    def __init__(self, car_brand, horse_power, color):
        self.car_brand = car_brand
        self.horse_power = horse_power
        self.color = color
        self.xPosition = 5
        self.yPosition = 5


    def drive(self, x, y):
        # Self benuntz man um Objekte zu referenzieren
        self.xPosition += x
        self.yPosition += y

    def print_position(self):
        print("Aktuelle Position des Autos: x="
              + str(self.xPosition) + " | y= "
              + str(self.yPosition))


print("Hello")
car1 = Car("Mercedes", 300, "Silber")
print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car1.print_position()
car1.drive(5, 10)
car1.print_position()

car2 = Car("Merces", 300, "Silber")


print(car2.car_brand)
print(car2.horse_power)
print(car2.color)

car3 = car1
car3.horse_power = 100

print(car1.horse_power)
print(car2.horse_power)
print(car3.horse_power)
