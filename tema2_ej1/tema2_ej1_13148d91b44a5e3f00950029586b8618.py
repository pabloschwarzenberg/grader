import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

while True:
    print("Seleccione una figura:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

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
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
