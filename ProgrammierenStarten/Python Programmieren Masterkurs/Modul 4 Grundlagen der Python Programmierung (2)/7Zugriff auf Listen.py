'''
------Zugriff auf Listen
numbers= [3,7,12,1,37]
print(type(numbers))

names = ["Hendrik", "Janek", "Anna", "Daniel",
         "Felix",3,4.2]


print(names[0])

------Merken:
- Wenn du mit ein positives Index von vorne her zielst,
dann startet man immer bei 0 und wenn man mit den
negativen Index von der Ende einer
Liste fängt zu zählen, dann startet man
bei -1.

--- Was bedeutet type?
- In Python gibt der Befehl type den Datentyp
eins Objekts zurück. Wenn du zum Beispiel
type(10) eingibst, erhälst du <class 'int'>,
weil 10 iene ganze Zahl ist. Es hilft dir herauszufinden,
welcher Typ eine Vriable oder ein Wert hat.
'''

numbers = [3,7,12,1,37]
print(type(numbers))

names= ["Hendrik", "Janek", "Anna", "Daniel", "Felix", 3, 4.2]
print(names)

print(names[1:5])
print(names[:4])
print(names[3:])



