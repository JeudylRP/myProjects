'''
------- 6. NAMENSKONVENTIONEN ------
'''


class Car:
    def __init__(self, car_brand, horse_power, color):
        self.car_brand = car_brand
        self.horse_power = horse_power
        self.color = color
        self.xPosition = 5
        self.yPosition = 5

    def drive(self, x, y):
        # self benutzt mauum Objekte zu referenzieren
        self.xPosition += x
        self.yPosition += y

    def print_position(self):
        print("Aktuelle Postion des Austos x="
              + str(self.xPosition) + " | y="
              + str(self.yPosition))

print("Hello")
car1 = Car("Mercedes",300, "Silber")
print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car1.print_position()
car1.drive(5,10)
car1.print_position()

car2 = Car("Mercedes", 300,"Silber")

print(car2.car_brand)
print(car2.horse_power)
print(car2.color)

car3 = car1
car3.horse_power = 100

print(car1.horse_power)
print(car2.horse_power)
print(car3.horse_power)











