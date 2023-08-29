import math

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_rectangulo(base, altura):
    return base * altura



def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    print("¡Bienvenido al programa de cálculo de áreas!")
    print("Selecciona una figura geométrica:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingresa el número de la figura: "))

    if opcion == 1:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        print("El área del rectángulo es:", resultado)
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        print("El área del triángulo es:", resultado)
    elif opcion == 3:
        diagonal1 = float(input("Ingresa la diagonal 1 del rombo: "))
        diagonal2 = float(input("Ingresa la diagonal 2 del rombo: "))
        resultado = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", resultado)
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        resultado = area_circulo(radio)
        print("El área del círculo es:", resultado)
    else:
        print("Opción inválida. Por favor, selecciona una opción válida del menú.")

           