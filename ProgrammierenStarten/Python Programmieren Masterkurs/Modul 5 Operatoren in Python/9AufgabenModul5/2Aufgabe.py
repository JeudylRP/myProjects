'''
------AUFGABE 2:

- BMI: Dody-Mass-Index:
In dieser Aufgabe sollst di einen sogennanten BMI-Rechner programmieren.
Ein BMI-Rechner berechnet anhand gewisser Werte, die vom Nutzer abgefragt werden,
dessen BMI.

Schreibe also ein Programm, welches alle für die BMI-Berechnung
notwendigen Daten com Nutzer einliest, anschliessend die entsprechende
Berechnung durchführt und daraufhin das Ergednis auf der Konsole
ausgibt. Da ein Programmierer gut darin sein muss, sich alle
notwendigen Informationen selbständig zu recherchieren, verrate ich
dir an dieser Stelle nicht. wie man den BMI im Detail berechner
(Tipp: Google ist als Programmierer dein bester Freund!
Mache also Gebrauch davon)

- Untergewicht: BMI < 18,5
- Normalgewicht: BMI 18,5-24,9
- Übergewicht: BMI 25-29,9
- Adipositas (Fettlebigkeit): BMI>=30



gewicht = float(input("Gebe dein Gewicht in Kilogramm ein: "))
groesse = float(input("Gebe deine Grösse in Metern ein: "))

bmi = gewicht/(groesse**2)

if bmi < 18.5:
    print("Du hast Untergewicht :(")
elif 18.5 <= bmi < 25:
    print("Du hast Normalgewicht")
elif 25 <= bmi < 29.9:
    print("Du hast Übergewicht")
else:
  print ("Du hast Adipositas :(")
print("Du wiegst "+str(gewicht)+" KG")
print ("Du bist "+str(groesse)+ "m gross")
print ("Dein BMI: "+str(bmi))
'''

weight = float(input("Körpergewicht in KG engeben:"))
height = float(input("Körpergrüsse in m eingeben"))

bmi = weight/(height*height)

print("Dein BMI ist: " +str(bmi))