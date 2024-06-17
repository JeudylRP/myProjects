'''def say_hello(first_name, last_name):
    print(print("Hallo " + first_name + " " + last_name))
    print("Willkommen zurück")

# Funktionsaufruf außerhalb der Funktionsdefinition
print(say_hello("Susi", "Mustermann"))

# in Python ist es so  dass jede Funktion immer einen Wert zurrückgibt
#und auch diese Printfunktion gibt deshalb immer den Wert "None" zurrück ,
# da er für nichst steht bzw. für die Abwesenheit eines Wertes, dennoch ein gültiger Wert ist
'''
'''
def say_hello(first_name, last_name):
    print("Hallo " + first_name + " " + last_name)
    print("Willkommen zurück")

print(type(say_hello("Susi", "Mustermann")))
'''
'''
Merken: 
Imeer wenn du zwangsweise ein Wert benötigst zum Aktuellen Zeitpunkt aber keinen
Sinnvollen Wert hast, dann  verwende 'None' und da wir bei der definierten Funktion
gar kein rückgabewert benötigt haben (jeder Funktion aber einen Wert zurrückgeben muss),
wird automatiscchdas Wert 'None' zurückgegeben
'''
'''
----- RETURN:
Sobald diese Schlüsselwort 'Return' innerhalb eines Funktionskörpers
aufgerufen wird, dann wird die Funktion sofort beendeet und entsprechend 
nach Return Folgende Wert  wird darufhin zurückgegeben.
'''


def maximum(a, b):
    if a < b:
        return b
    else:
        return a


result = maximum(45, 9)
print(result)
