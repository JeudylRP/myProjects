def calcular_imc(peso, altura):
    """
    Calcular el Índice de Masa Corporal (IMC).

    Parámetros:
    peso (float): Peso en kilogramos
    altura (float): Altura en metros

    Retorna:
    float: IMC calculado
    """
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    """
    Clasificar el IMC en categorías estándar.

    Parámetros:
    imc (float): Índice de Masa Corporal calculado

    Retorna:
    str: Categoría del IMC
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = calcular_imc(peso, altura)
        categoria = clasificar_imc(imc)
        print(f"Su IMC es: {imc:.2f}")
        print(f"Categoría: {categoria}")
    except ValueError:
        print("Por favor, ingrese números válidos para el peso y la altura.")