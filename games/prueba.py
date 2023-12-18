def add(x, y):
    """Suma x e y."""
    return x + y

def subtract(x, y):
    """Resta y de x."""
    return x - y

def multiply(x, y):
    """Multiplica x e y."""
    return x * y

def divide(x, y):
    """Divide x por y."""
    if y == 0:
        return "Error: División por cero."
    return x / y

def calculator():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    choice = input("Selecciona una operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculator()
