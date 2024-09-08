'''
------- 4. Die Super()-Funktion
Fortgeschrittene Objektorientierung - Vererbung. Die super()-Funktion
'''


class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name  # Speichert den namen des Tieres
        self.age = age  # Speichert das Alter des Tieres
        self.color = color  # Speichert die Farbe des Tieres
        self.fav_food = fav_food  # Speichert das Lieblings des Tieres

    def sleep(self):
        print("Ich schlafe gerade...")  # Wenn das Tier schläft, zeigt es diesen Text an

    def move_fast(self): print("Aktuelle Gesdchwindigkeit 20km/h")


class Dog(Animal):
    def bark(self):
        print("Wau Wau")  # Wenn der Hnund bellt, zeigt es diesen Text an


class Cat(Animal):
    def purr(self):
        print("Schnurr Schnurr")  # Wenn die Katze schnurrt, zeigt es diesen Text an


class Tiger(Animal):
    def move_fest(self):
        print("Aktuelle Geschwindigkeit: 80km/h")


class Owl(Animal):
    def __init__(self, name, age, color, fav_food, hunting_instinct):
        super().__init__(name, age, color, fav_food)
        self.hunting_instinct = hunting_instinct

    def sleep(self):
        super().sleep()
        print("Gleichgewicht halten ...")


dog = Dog("Bello", 4, "braun", "Fleisch")
tiger = Tiger("Tigris", 5, "Orange", "Fleisch")
owl = Owl("Eule", 12, "grau", "Würmer", 7)

print(owl.name)
print(owl.hunting_instinct)

owl.sleep()
dog.move_fast()
tiger.move_fast()
'''
Wenn eine Klasse spezifische Attribute haben soll, 
die nicht von der Elternklasse vererbt werden, dann 
überschreibt man einfach die __init__-Methode der Klasse. 
'Man ruft zu Beginn die super()-Methode auf, um die 
Standard-Attributwerte der Elternklasse zu initialisieren, 
und übergibt die entsprechenden Parameter nach oben an die 
Elternklasse. Anschließend definiert man noch die spezifischen 
Attribute für die Klasse, die man zusätzlich zu 
den vererbten Attributen haben möchte.

----Was ist die Super funktion():
Stellt dir vor, du baust 
'''