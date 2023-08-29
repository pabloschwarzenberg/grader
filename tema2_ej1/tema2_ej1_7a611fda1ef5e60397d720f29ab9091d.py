import math

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el área de un rombo
def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2

# Menú principal
while True:
    print("Selecciona una figura geométrica para calcular su área:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    print("5. Salir")

      opcion = int(input("Ingresa el número de opción: "))

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
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

