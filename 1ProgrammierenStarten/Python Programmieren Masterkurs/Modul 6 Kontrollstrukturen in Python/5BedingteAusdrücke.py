'''
------ BEDINGTE AUSDRÜCKE
'''
bill = 10

tip = float(input("Rechnung: " + str(bill) +
                  " Euro, wie viel Trinkgeld möchten"
                  " Sie geben: "))
if tip < bill * 0.1:
    print("Vielen Dank!")
else:
    print("Wow, vielen lieben Dank! "
          "Sehr grosszügig")
# A if Bedingung else B
print ("Vielen Dank!") if tip < bill * 0.1 else print("Wow, vielen lieben Dank! "
        "Sehr grosszügig")