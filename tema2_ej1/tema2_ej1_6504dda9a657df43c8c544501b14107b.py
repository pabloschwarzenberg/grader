import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("1. Calcular área del rectángulo")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del rombo")
    print("4. Calcular área del círculo")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")