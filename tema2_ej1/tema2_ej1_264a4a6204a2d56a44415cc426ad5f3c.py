from math import pi
def area_triangulo(base, altura):
    Area = (base * altura)/2
    return Area

def area_rectangulo(base, altura):
    Area = base * altura
    return Area

def area_rombo(diagonal1, diagonal2):
    Area = (diagonal1 * diagonal2)/2
    return Area

def area_circulo(radio):
    Area = (pi * radio**2)
    return Area