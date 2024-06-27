'''
------- FUNKTIONEN MIT RÜCKGABEWERTEN DEFINIEREN UND DER DATENTYP NONETYPE
'''
'''
def greeting(first_name, last_name):
    print(print("Hallo "+ first_name+" " + last_name))
    print("Schön das du wieder da bist!")
    print("Ich wünsche dir viel Spass beim Programmieren!")

print(type(greeting("Klaus", "Mustermann")))
# None= Nichts, Er esteht für die Abwesenheit eines Wertes.
'''


def maximum(a, b):
    if a < b:
        return b
    else:
        return a
result = maximum(5, 3)
print(result)
