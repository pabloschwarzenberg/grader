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
    opcion = input("Menú:\n1. Calcular área de un triángulo\n2. Calcular área de un rectángulo\n3. Calcular área de un rombo\n4. Calcular área de un círculo\nSeleccione una opción: ")

    if opcion == "1":
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == "3":
        diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
        area = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", area)
    elif opcion == "4":
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

