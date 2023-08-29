import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("Calculadora Geométrica")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(base, altura))
    elif opcion == 3:
        diagonal1 = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal2 = float(input("Ingrese la diagonal menor del rombo: "))
        print("El área del rombo es:", area_rombo(diagonal1, diagonal2))
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
    else:
        print("Opción inválida")