'''
------ Bitweise Operatoren:
1. Ermöglichen das gezielte Verändern einzelner
Bits eines Wertes.
2. Umgang mit Bitweisen Operatoren fällt
Einsteigern häufig schwer.
3. Grund:
- Bitweise Operatoren beziehen sich immer
auf die Darstellung von Zahlen im Dalsystem.
- Menschen sind gewohnt,mit Zahlen im Dezimalsystem
zu arbeiten (z.B. 8 oder 19)
4. Hinweis: Bonus Modul zum Thema Zahlensysteme

--- Tabelle:
1. Operator: <<; >>; &; |; ^.
2. Beschreibung: Linksshift (alle Bits nach links
schueben); Rechtsshift (alle Bits nach rechts schieben);
UND-Operator; ODER-Operator; Exklusiv-ODER-Operator.
3. Beispiel:x<<1 x<<4; x>>1 x>>4; 2&3; 2|3; 2^3
'''

'''
print(6)
print(6  << 1) #Dualsystem: 0000 0110 == 6
                        #   0000 1100 == 12
'''
'''
print(6>>1) #Dualsystem: 0000 0110 == 6
                      #  0000 0011 == 3
'''
'''
----- Bitmanipulation:
UND-Operator(Einzelne Bits auf 0 setzen,
während die anderen Bits unverändert bleiben).

print(6 und 0xFD)

Nebenrechnung:

0000 0110 (6) AND 1111 1101 (0xFD)
= 0000 0100 = 4 

--- Funktion der Maske:
- Alle Bits die in der Maske "0" sind,
werden auf "0" gesetz.
- Alle Bits die in der Maske auf "1" sind
bleiben unverändert.
'''
'''
print(6 & 0xFD)
'''
'''
---BITMANIPULATION ODER-OPERATOR:
(Einzelne Bits auf "1" setzen, während
die anderen Bits unverändert bleiben)

print(6|0x01)

Nebenrechnung:
0000 0110(6) OR 0000 0001(0x01) = 0000 0111 == 7

--- Funktion deere Maske:
- Alle Bits die in der Maske "1" sind, 
werden auf "1" gesetz.

- Alle Bits die in der Maske auf "0" sind, 
bleiben unverändert.
'''
'''
print (6|0x01)

------ BITMANIPULATION: EXKLUSIV-ODER-OPERATOR.
(Bits werden invertiert)

print(6^0x0F)

Nebenrechnung: 

(6) 0000 0110 UND EX 0000 1111 
= 0000 1001 == 9

--- Funktion der Maske:
-Alle Bits die in der Maske "1" sind, werden
invertiert.
- Alle Bits die in der Maske auf "0" sind,
bleiben unverändert
'''

print (6 ^ 0x0F)






