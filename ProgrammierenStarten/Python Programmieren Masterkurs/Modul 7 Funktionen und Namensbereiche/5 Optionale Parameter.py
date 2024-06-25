'''
-------OPTIONALE PARAMETER
'''
'''
for x in range(2, 5, 2):
 print(x)
'''

def greeting(first_name, last_name, academic_title = "Dr.Dr. "):
    if academic_title != "":
       academic_title += " "
    print("Hallo "+academic_title+first_name+" "+ last_name)
    print("Schön dass du da bist!")
greeting("Max", "Mustermann")