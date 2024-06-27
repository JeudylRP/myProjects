'''
------- 3. WAS HAT ES MIT DEM PARAMETER "self" AUF SICH?



'''

'''
------- Veranscahulischung: Was ist eine Referenz?
Beispiele:

                                                 Speicher
                                                |   
car1 = Car() #Car Objekt 1 -------------------->|Star-Adresse
                                                | 
     Speicherbereich, in                        |                                               
     welchem alle Daten                         |
     des erzeugten Objekts                      |        
    gespeichert sind                            |
                                                |
car2 = Car() #Car Objekt 2 -------------------->|Start-Adresse 
'''

class Car:
   def __ini__(self):
       self.car_brand = None
       self.horse_power = None
       self.color = None
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


car3 = car1
car3.horse_power = 100

print(car1.horse_power)
print(car2.horse_power)
print(car3.horse_power)



