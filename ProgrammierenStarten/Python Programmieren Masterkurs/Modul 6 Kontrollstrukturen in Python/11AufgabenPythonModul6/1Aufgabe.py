'''
-------AUFGABE 1:
--- Schreibe ein Programm, welches die Zahlen von
1 bis 100 auf der Konsole ausgibt. Jede Zahl
soll dabei in einer separaten Zeile ausgegeben werden.
Nun gilt es das Programm noch etwas zu erweitern. Und zwar
sollst du jede Zahl, die durch 3 teilbar ist,
durch den Satz "teilbar durch 3" ersetzen.
Jede Zahl, die durch 4 teilbar ist, soll
durch den Satz "teilbar durch 4 ersetzt werden".
JETZT WIRD ES EINIGE zAHLEN GEBEN; DIE  SOWOHL DURCH 3
als auch durch 4 teilbar sind (z.B. die 12).
Bei diesen Zahlen soll dann "teilbar durch 3 und 4"
ausgegeben werden.

'''

def print_numbers():
    for i in range(1,101):
        if i % 3 == 0 and i % 4 == 0:
            print("TEILBAR DURCH 3 UND 4: "+str(i))
        elif i % 3 == 0:
           print("TEILBAR DURCH 3: "+str(i))
        elif i % 4 == 0:
            print("TEILBAR DURCH 4: "+str(i))
        else:
            print("Es ist nicht teilbar durch 3 oder 4: "+str(i))
print_numbers()























