'''
------- 8. BELIEBIGE ANZAHL VON PARAMETERN AN
FUNKTIONEN ÜBERGEBEN.
'''

def multiply(number1, number2, *numbers):
    sum= number1 * number2
    for i in numbers:
        sum *= i
    return sum

print(multiply(2,2,2,2))












