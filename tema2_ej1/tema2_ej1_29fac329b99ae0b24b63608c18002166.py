import math

def area_triangulo(base,altura):
    base = int(base)
    altura = int(altura)
    return base * altura / 2

def area_rectangulo(base,altura):
    base = int(base)
    altura = int(altura)
    return base * altura

def area_rombo(diagonal1,diagonal2):
    diagonal1 = int(diagonal1)
    diagonal2 = int(diagonal2)
    return diagonal1 * diagonal2 / 2

def area_circulo(radio):
    r = int(radio)
    a = r * r * math.pi
    return a           