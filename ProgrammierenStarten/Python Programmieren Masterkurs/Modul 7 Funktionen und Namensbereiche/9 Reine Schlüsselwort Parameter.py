'''
9. REINE SCHLÜSSELWORT PARAMETER
'''
'''
def multiply(number1, number2, *numbers):
    sum = number1*number2
    for i in numbers:
         sum *= i
    return sum

print(multiply(2,2,2,2))
'''
'''
def xyz(valu1, valu2, *values, parameter1):
     print("Test", end = ", ")
print("siehst du")

print("test", "siehst","d","u", sep)
'''

print("Test", end=", ")
print("siehst du")

print("test", "siehst", "d", "u", sep="-")



