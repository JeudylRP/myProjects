'''
----- DER SELF PARAMETER
'''
class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None

car1 = Car()
print(car1.car_brand)
car1.car_brand = "Audi"
car1.horse_power = 250
car1.color = "Blau"

print (car1.car_brand)
print(car1.horse_power)
print(car1.color)

car2= Car()
car2.car_brand = "BMW"
car2.horse_power = 210
car2.color = "Schwarz"


car3= car1


print(car1)
print(car2)
print(car3)
print(car1.horse_power)
print(car3.horse_power)


'''
Bei ieser kryptischen Zhal am Ende handelt es sich um eine sogenannte referenz.
Denn sobald  wir ein Objekt erzeugen wird im Computer Speicherplatz für diese Objekt reserviert
und auf diesen reservierten Speicher werden die eilnen Attribute  und somit die Daten des Objektes 
Gespeichert, weil die Informationen irgenwo abgelgt werden damit man später zum Beispiel wieder darauf 
zugreifen kann.

---MERKEN- REFERENZ:
Wenn wir ein Objekt erzeugen  dann wird intern Speicher reserviert, an diesem wird der Reihe nach
alle Daten ds entsprechenden Objekt abgespeichert und die Adresse die wir bei dem Objekt erzeugung.
'''


'''
---REFERENZ LAUT CHATGPT:
Eine Referenz in der Programmierung ist eine Art Verweis oder Zeiger auf einen Speicherort,
der ein bestimmtes Objekt oder eine bestimmte Variable enthäl. 
Anstatt den eigentlichen Wert zu kopieren, wird nur die Adresse des Wertes übergeben oder verwendet.

Dies ermöglicht es, dass mehrer Variablen auf dasselbe Objekt oder
dnselben Speicherbereich zeigen können. 
Änderungen an einem Obkjekt über eine Referenz wirken sich somit auf alle Referenzen dieses Objekts aus.
Hier sind einige wichtige Punkte zu Referenten:
denselben Speicherbereich zeigen können.
Änderungen an einem Objekt über eine Referenz wirken sich somit
auf alle Referenzen diese Objekts aus.

Hier sind einige wichtige Punkte zu Referenzen:

- 1. Speicherverwaltung: 
Referenzen ermöglichen eine effiziente Speicherverwaltung,
da sie verhindern, dass Daten unnötig kopiert werde.

-2. Objektmanipulation:
Über Referenzen können Objekte direkt manipuliert werden,
ohne dass dise kopiert werden müssen. 

-3. Mehrere Verweise: 
Mehrere Referenzen können auf dasselbe Objekt zeigen,
sodass Änderungen über eine Referenz auch für alle andren sichtbar sind.

WICHTIG:
In python liest man normalerweise den Code von Links nach rechts,
ähnlich wie den meisten Programmiersprachen

--- Was bedeutet Instanzieren?
Das "Instanzieren wird in der Programmierung verwendet, um den Prozess zu beschreiben,
bei dem ein Objekt einer Klasse erstellt wird.

Dabei wird eine speziphische Instanz eines Objekts erzeugt, das die Eigenschaften und Methoden
der Klasse besitzt"
'''




