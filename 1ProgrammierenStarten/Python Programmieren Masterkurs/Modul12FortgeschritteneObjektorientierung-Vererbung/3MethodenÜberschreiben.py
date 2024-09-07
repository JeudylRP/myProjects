'''
------- 3. Methoden Überschreiben 00:00
'''

class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Ich schlafe gerade ...")


class Dog(Animal):
    def bark(self):
        print("Wau Wau")

class Cat(Animal):
    def purr(self):
        print("Schnurr Schnurr")

dog = Dog("Bello", 4, "braun", "Fleisch")
dog.sleep()
print(dog.name)
dog.bark()

cat = Cat("Kitty", 10,"braun", "Fisch")
cat.purr()
print(cat.name)
print(cat.age)




