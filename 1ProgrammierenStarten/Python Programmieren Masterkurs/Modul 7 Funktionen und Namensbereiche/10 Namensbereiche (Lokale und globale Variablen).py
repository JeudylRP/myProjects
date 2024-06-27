'''
-------10. NAMENSBEREICHE (LOKALE UND GLOBALE VARIABLEN)
'''
def add(number1, number2):
    global test
    test = 11
    res = number1 + number2
    print(test)
    return res

test= 10
print(add(2, 3))
print(test)












