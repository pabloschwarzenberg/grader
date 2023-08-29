import math

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return 0.5 * base * altura

# Función para calcular el área de un rombo
def area_rombo(diagonal_1, diagonal_2):
    return 0.5 * diagonal_1 * diagonal_2

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2

# Menú para escoger qué figura se desea calcular
print("Calculadora de figuras geométricas")
print("1. Rectángulo")
print("2. Triángulo")
print("3. Rombo")
print("4. Círculo")
opcion = int(input("Ingrese el número de la figura que desea calcular: "))

# Lectura de los parámetros necesarios para cada figura
if opcion == 1:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = area_rectangulo(base, altura)
    print("El área del rectángulo es:", area)
elif opcion == 2:
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = area_triangulo(base, altura)
    print("El área del triángulo es:", area)
elif opcion == 3:
    diagonal_1 = float(input("Ingrese la primera diagonal del rombo: "))
    diagonal_2 = float(input("Ingrese la segunda diagonal del rombo: "))
    area = area_rombo(diagonal_1, diagonal_2)
    print("El área del rombo es:", area)
elif opcion == 4:
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print("El área del círculo es:", area)
else:
    print("Opción inválida. Intente de nuevo.")