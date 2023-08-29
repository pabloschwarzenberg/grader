import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("Seleccione la figura geométrica:")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingrese el número de la figura: "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        radio = float(input("Ingrese el radio del círculo: "))

    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        radio = float(input("Ingrese el radio del círculo: "))

    elif opcion == 3:
        diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
        area = area_rombo(diagonal1, diagonal2)
        radio = float(input("Ingrese el radio del círculo: "))

    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        radio = float(input("Ingrese el radio del círculo: "))

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del 1 al 4.")
