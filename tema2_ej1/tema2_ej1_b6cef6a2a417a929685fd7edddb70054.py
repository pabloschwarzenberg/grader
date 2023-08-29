import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

figura = input("Ingrese el nombre de la figura: ")
if figura == "triángulo":
    base = float(input("Ingrese la longitud de la base: "))
    altura = float(input("Ingrese la longitud de la altura: "))
    print("El área del triángulo es:", area_triangulo(base, altura))
elif figura == "rectángulo":
    base = float(input("Ingrese la longitud: "))
    altura = float(input("Ingrese la anchura: "))
    print("El área del rectángulo es:", area_rectangulo(base, altura))
elif figura == "rombo":
    diagonal1 = float(input("Ingrese la diagonal 1: "))
    diagonal2 = float(input("Ingrese la diagonal 2: "))
    print("El área del rombo es:", area_rombo(diagonal1, diagonal2))
elif figura == "círculo":
    radio = float(input("Ingrese el radio: "))
    print("El área del círculo es:", area_circulo(radio))
else:
    print("Nombre de figura inválido")      