'''
------ AUFGABE 2:
- Mal angenommen wir haben innerhalb unseres
Programms folgenden Code gegeben:
first_names = ["Max","Fritz","Anna"]
last_names = ["Mustermann", Huber, "Neumann"]
Deine Aufgabe ist es nun, dieses Programm dahingehend
zu erweitern, dass der Nutzer dazu aufgefordert wird,
den Wert 0 einzugeben, falls er den Namen von Max
Mustermann ausgeben lassen möchte, soll der Nutzer
hingegen dn Wert 1 eingeben und falls er den Namen
Anna Neumann ausgeben lassen möchte, soll er den Wert 2
eingeben.

Je nachdem wie sich der Nutzer entscheiden hat, soll dann der
entsprechende Name mithilfe der print()-Funktion und dem
Zugriff auf die entsprechenden Liste ausgegeben werden.

first_names = ["Max", "Fritz", "Anna"]
last_names = ["Mustermann","Huber","Neumann"]

#Benutzereingabe erfassen

print("1. Wert 0 eingeben = 'Max Mustermann'.\n"
      "2. Wert 1 eingeben = 'Fritz Huber'.\n"
      "3. Wert 2 eingeben = 'Anna Neumann'.\n")

auswahl = int
auswahl = int(input("Gebe ein Wert ein!: \n"))
(print("Du hast die Nummer "+str(auswahl)+" ausgewält"))
if auswahl== 0:
    print("Du hast "+first_names[auswahl] +" "
          +last_names[auswahl]+ " ausgewählt")
elif auswahl == 1:
    print("Du hast " + first_names[auswahl] + " "
          + last_names[auswahl] + " ausgewählt")
elif auswahl == 2:
    print("Du hast " + first_names[auswahl] + " "
          + last_names[auswahl] + " ausgewählt")
else:
 print("Nur Zahlen zwischen 0 und 2")
'''


first_names = ["Max","Fritz","Anna"]
last_names = ["Mustermann","Huber","Neumann"]

output = int(input("Bitte eine Zahl zwischen 0 und 2 eingeben: "))
print(first_names[output]+ " " +last_names[output])




