'''
------ Die Schlüsselwörter break und continue
'''

password = "passwort123"
user_input = ""
counter = 0
while user_input != password:
    #if counter == 3:
     #   break
    user_input = input("Bitte gebe das korrekte Passwort ein: ")
    print ("Du hast es "+str(counter+ 1)+" Mal versuch")

    counter += 1
else:
    print("Das Passwort wurde erfolgreich eingegeben...")

while True:
    name = input("Bitte Nutzernamen eingeben: ")
    if(name) != "testUser":
        continue
    user_input = input ("Hallo testUser, was ist dein Passwort?: ")
    if(user_input == password):
        break

print("testUser wurde erfolgreich eingelogt!")









