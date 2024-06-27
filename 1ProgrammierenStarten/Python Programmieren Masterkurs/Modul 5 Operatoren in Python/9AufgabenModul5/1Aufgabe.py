'''
------AUFGABE 1:
Wenn man im Supermarkt an einer Kasse arbeitet, hat man
neben der Tätigkeit des Kassieren ausch die Aufgabe,
für gewisse Produkte das Alter des Kundes zu prüfen (z.B
Tabakwaren, Alkohol). Hierzu muss der Kunde seine Personalausweis
vorzeigen, auf welchem sein Geburtdatum angegeben ist.
Auf Basis des Jahrgangs in wenigen Sekunden zu entscheide, ob
der Kunde nun schon 18 Jahre oder älter ist, kann häufig
zu fehlern führen.







 current_year = 2024
 year_of_birth = int(input("Jahrgang eingeben: "))

 print(current_year - year_of_birth >=18)
'''
from datetime import datetime
aktuellesJahr = datetime.now().year

geburtsjahr =int(input("Gebe dein Geburtsjahr ein: "))

alter =aktuellesJahr-geburtsjahr

if alter >= 18:
    print("Du kannst Erwachsene-Produkte kaufen. "
          "Du bist: "+str(alter)+" jahre alt. ")
else:
    print("Es tut mir leid du bist ein "
          "Baby. Du bist: "+str(alter)+" jahre alt")

print("- Aktuelles Jahr: "+str(aktuellesJahr)+".") #String-Konkatenation
print("- Du bist im Jahr: "+ str(geburtsjahr)+" geboren.")




