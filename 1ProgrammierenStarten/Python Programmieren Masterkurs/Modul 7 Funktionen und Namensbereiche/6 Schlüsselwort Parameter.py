'''
------- SCHLÜSSELWORT PARAMETER
'''
def greeting(first_name, last_name, academic_title= ""):
    if academic_title != "":
        academic_title += " "
    print("Hallo "+ academic_title + first_name + " " + last_name)
    print("Schön dass du da bist!")

greeting(first_name = "Max", last_name= "Mustermann", academic_title= "Dr.")

greeting(academic_title ="Dr.", first_name="Max", last_name="Mustermann"  )