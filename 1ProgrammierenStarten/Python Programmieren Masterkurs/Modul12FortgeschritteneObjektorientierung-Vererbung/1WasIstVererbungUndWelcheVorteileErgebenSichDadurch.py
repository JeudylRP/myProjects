'''
-------1. Was ist Vererbung und welche Vorteile ergeben sich dadurch?
--- Was ist Vererbung und Welche Vorteile ergeben sich dadurch?
'''


class Dog:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Ich schlafe gerade...")

    def bark(self):
        print("Wau Wau")


class Cat:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print("Ich schlafe gerade...")

    def purr(self):
        print("Schnurr Schnurr")


'''
---UML-Klassendiagramm
-UML = Uniform Modeling Language
- Standardisierte Beschreibungssprache von Strukturen und Abläufeen in objektorientierten Programmiersprachen

--- UML-Klassendiagramm unseres aktuellen Code Beispiels


----------
Animal
name:str
color:str
fav_food: str
--------------|



|
|
|
!^


------
Dog
------
name: str
age: int
color: str
fav_food: str
--------------|
sleep():None   
bark(): None
------


------
Cat
------
name:str
age:int
color:str
fav_food:str
---------|
sleep():None
purr():None
------

'''
