'''
------- EINSCHUB: LISTE VS. TUPEL (VERÄNDERLICH VS. UNVERÄNDERLICH)
---- Was sind Tupel?
1. Listen sind veränderliche Datenstrukturen.
2. Tupel sind unveränderliche Datenstrukturen.
3. Werte eines Tupels können im Vergleich zu Listen also nicht
mehr im nachinein modifiziert werden.
'''
'''
def greeting(first_name, last_name, academic_title=""):
    if academic_title != "":
        academic_title += " "
    print("Hallo " +academic_title + first_name + " " + last_name)
    print("Schön das du da bist!")

greeting(first_name="Max", last_name="Mustermann", academic_title="Dr." )
greeting("Max", academic_title= "Dr.", last_name="Mustermann")
'''
'''
list1 = [1, 3, 4, 8]
print(list1)

list1[1] = 10
print(list1)

tupel1 = (1, 3, 4, 8)
print(tupel1)

tupel2 = (2,)
print((tupel2))
'''
'''
person1= ("Max","Mustermann",28)

#first_name = person1[0]
#last_name = person1[1]
#age = person1[2]
first_name, last_name, age = person1

print(first_name)
print(last_name)
print(age)
'''

def generate_password(name,age):
#Aus übergebenen Namen und dem Alter
# mehrere PasswortKombinationen generieren.
 return("passwort1", "passwort2", "passwort3")
password1, password2, password3 =generate_password("Max", 20)

print(password3)






