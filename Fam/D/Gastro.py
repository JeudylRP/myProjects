def calcular_imc(peso, altura):
    """
    Esta función calcula el Índice de Masa Corporal (IMC).

    Parámetros:
    peso (float): El peso de la persona en kilogramos.
    altura (float): La altura de la persona en metros.

    Retorna:
    float: El valor del IMC calculado.
    """
    imc = peso / (altura ** 2)  # Fórmula para calcular el IMC: peso dividido por la altura al cuadrado
    return imc  # Devolver el IMC calculado


def clasificar_imc(imc):
    """
    Esta función clasifica el IMC en categorías.

    Parámetros:
    imc (float): El valor del IMC calculado.

    Retorna:
    str: La categoría en la que cae el IMC.
    """
    if imc < 18.5:
        return "Bajo peso"  # Si el IMC es menor que 18.5, está en la categoría de "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"  # Si el IMC está entre 18.5 y 24.9, está en la categoría de "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"  # Si el IMC está entre 25 y 29.9, está en la categoría de "Sobrepeso"
    else:
        return "Obesidad"  # Si el IMC es 30 o más, está en la categoría de "Obesidad"


if __name__ == "__main__":
    try:
        # Solicitar al usuario que ingrese su peso y altura
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        # Calcular el IMC usando los valores ingresados
        imc = calcular_imc(peso, altura)

        # Clasificar el IMC calculado
        categoria = clasificar_imc(imc)

        # Mostrar el IMC y su categoría
        print(f"Su IMC es: {imc:.2f}")
        print(f"Categoría: {categoria}")
    except ValueError:
        # Si el usuario ingresa un valor no numérico, mostrar un mensaje de error
        print("Por favor, ingrese números válidos para el peso y la altura.")
