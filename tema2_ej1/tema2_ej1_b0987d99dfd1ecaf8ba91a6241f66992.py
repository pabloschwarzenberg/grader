import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return 0.5 * diagonal_mayor * diagonal_menor

def calcular_area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("¡Bienvenido a la Calculadora Geométrica!")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")

    opcion = int(input("Ingrese el número correspondiente a la figura geométrica de la que desea calcular el área: "))

    if opcion == 1:
        base = float(input("Ingrese el valor de la base del rectángulo: "))
        altura = float(input("Ingrese el valor de la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo con base", base, "y altura", altura, "es:", area)
    elif opcion == 2:
        base = float(input("Ingrese el valor de la base del triángulo: "))
        altura = float(input("Ingrese el valor de la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo con base", base, "y altura", altura, "es:", area)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo con diagonal mayor", diagonal_mayor, "y diagonal menor", diagonal_menor, "es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el valor del radio del círculo: "))
        area = calcular_area_circulo(radio)
        print("El área del círculo con radio", radio, "es:", area)
    else:
        print("Opción inválida. Por favor, seleccione un número válido correspondiente a la figura geométrica del menú.")