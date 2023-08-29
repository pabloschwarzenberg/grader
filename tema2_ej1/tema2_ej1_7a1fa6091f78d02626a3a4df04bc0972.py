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
    print("¿Qué figura deseas calcular?")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingrese el número de la figura: "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))
    elif opcion == 3:
        diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
        print("El área del rombo es:", area_rombo(diagonal1, diagonal2))
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
    else:
        print("Opción inválida. Por favor, seleccione un número válido.")
