PI = 3.141592653589793
def addition(a, b):
    return a + b

def faculty(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial
