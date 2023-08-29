from math import pi
def area_triangulo(base,altura):
    a = (base * altura)/2
    return a
def area_rectangulo(base,altura):
    a = base * altura
    return a

def area_rombo(diagonal1,diagonal2):
    a = (diagonal1 * diagonal2)/2
    return a

def area_circulo(radio):
    a = pi * (radio**2)
    return a
