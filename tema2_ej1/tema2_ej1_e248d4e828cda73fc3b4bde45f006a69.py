#Calculadora Geométrica
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

if __name__ == "__main__":
    # Menú de opciones para el usuario
    print("1. Calcular área de un rectángulo")
    print("2. Calcular área de un triángulo")
    print("3. Calcular área de un rombo")
    print("4. Calcular área de un círculo")

    # Solicitar al usuario que seleccione una opción
    opcion = int(input("Ingrese el número de la opción deseada: "))

    # Calcular el área de un rectángulo
    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)

    # Calcular el área de un triángulo
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area)

    # Calcular el área de un rombo
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area)

    # Calcular el área de un círculo
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print("El área del círculo es:", area)

    # Mostrar mensaje si se selecciona una opción inválida
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")