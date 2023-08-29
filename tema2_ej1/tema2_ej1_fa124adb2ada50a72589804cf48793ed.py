import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio**2

def menu():
    while True:
        print("Seleccione la figura geométrica:")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Rombo")
        print("4. Círculo")
        print("5. Salir")