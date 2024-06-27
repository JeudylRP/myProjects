PI = 3.1415926535588783


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


if __name__ == "__main__":

    print("Hier komplette Ablauflogik, falls diese"
          "File als Hauptprogramm direkt ausgeführt"
          "wird.")
print(__file__)
