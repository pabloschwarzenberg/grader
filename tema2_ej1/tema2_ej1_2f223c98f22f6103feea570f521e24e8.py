import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("Calculadora Geométrica")
    print("1. Área de un rectángulo")
    print("2. Área de un triángulo")
    print("3. Área de un rombo")
    print("4. Área de un círculo")

    opcion = int(input("Selecciona una opción (1-4): "))

    if opcion == 1:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

           