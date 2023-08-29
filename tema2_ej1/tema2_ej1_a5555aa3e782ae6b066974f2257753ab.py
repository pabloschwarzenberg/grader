import math

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("1. Calcular área de un triángulo")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un rombo")
    print("4. Calcular área de un círculo")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        print("El área del triángulo es:", resultado)
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        print("El área del rectángulo es:", resultado)
    elif opcion == 3:
        diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
        diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
        resultado = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", resultado)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = area_circulo(radio)
        print("El área del círculo es:", resultado)
    else:
        print("Opción inválida")