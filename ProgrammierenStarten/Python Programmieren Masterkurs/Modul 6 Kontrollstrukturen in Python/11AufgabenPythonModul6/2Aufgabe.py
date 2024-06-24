'''
------- AUFGABE 2:
- In deiser Aufgabe sollst du einen einfahcen Tachenrechner
programmieren. Zunächst soll der Nutzer dazu aufgefordert werden,
zwei beliebige Zahlen in das Programm einzulesen.

Danach soll dr Nutzer mit einer dritten Eingabe entscheiden, welche
Operation auf diesen beiden zuvor eingelesenen Zahlen ausgeführt
werden soll. Dabei soll der Nutzer die Möglichkeit haben, die
beiden Zahlen miteinannder zu addieren, zu substrahieren, zu dividieren
oder zu multiplizieren.

Je nachdem für welche Operation sich der Nutzer entscheidet, soll
dann das entsprechede Ergebnis auf der Konsole
ausgegeben w

def taschenrechner():
    # Variablen
    num1 = float(input("Gib die erste Zahl ein: "))
    num2 = float(input("Gib die zweite Zahl ein: "))
    operation = input("Wähle die Operation (+,-,*,/): ")

    # Ausführen der entsprechenden Operation und Ausgabe des Ergebnisses
    if operation == "+":
        result = num1 + num2
        print(f"Das Ergebnis der Addition ist: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Das Ergebnis der Subtraktion ist: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Das Ergebnis der Multiplikation ist: {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Das Ergebnis der Division ist: {result}")
        else:
            print("ERROR, nicht durch 0 teilen!!")
    else:
        print("Ungültige Operation!")
taschenrechner()
'''

'''
------ MUSTERLÖSUNG:
'''

number1 = float(input("Gebe die erste Zahl ein: "))
number2 = float(input("Gebe die erste Zahl ein: "))
operation = input("Welche Operation (+,-,*,/)"
                  "soll durchgeführt werden:")
if(operation == "+"):
    print(number1 + number2)
elif(operation == "-"):
    print(number1 - number2)
elif(operation == "*"):
    print(number1 * number2)
elif(operation == "/"):
    print(number1 / number2)
else:
    print("Ungültige Operation!")























