'''
------ 8. Eine while-Schleife mit einem
else-Zweig kombinieren.
'''

password = "passwort123"
user_input = ""
counter = 0

while user_input != password:
    if counter == 3:
        break
    user_input = input("Bitte gebe das Korrekte Passwort ein: ")
    counter += 1
else:

    print("Das Passwort wurde erfolgreich eingegeben...")

print("Hier geht es weiter")
