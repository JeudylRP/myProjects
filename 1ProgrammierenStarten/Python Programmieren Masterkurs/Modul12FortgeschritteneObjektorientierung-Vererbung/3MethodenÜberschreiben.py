'''
------- 3. Methoden Überschreiben
'''


class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name  # Speichert den Naen des Tieres
        self.age = age  # Speichert das Alter des Tieres
        self.color = color  # Speichert die Farbe des Tieres
        self.fav_food = fav_food  # Speichert das Lieblings des Tieres

    def sleep(self):
        print("Ich schlage gerade...")  # Wenn das Tier schläft, zeigt es diesen Text an

    def move_fast(self):
            print("Aktuelle Geschwindigkeit: 20km/h")


class Dog(Animal):
    def bark(self):
        print("Wau Wau")  # Wenn der Hund bellt, zeigt es diesen Text an


class Cat(Animal):
    def purr(self):
        print("Schnurr Schnurr") #Wenn die Katze schnurrt, zeigt es diesen Text an

class Tiger(Animal):
    def move_fast(self):
        print("Aktuelle Geschwindigkeit: 80km/h")

dog = Dog("Bello", 4,"braum", "Fleisch")
tiger = Tiger("Tigris", 5, "Oraange", "Fleisch")

dog.move_fast()
tiger.move_fast()


