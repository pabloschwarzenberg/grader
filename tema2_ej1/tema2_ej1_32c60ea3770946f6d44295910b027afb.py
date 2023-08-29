def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
import math

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    return 0.5 * base * altura

# Función para calcular el área de un rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")
    
    opcion = int(input("Seleccione una opción (1-4): "))
    
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
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        area = area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        