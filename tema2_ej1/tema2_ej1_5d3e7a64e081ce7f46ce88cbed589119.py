import math
def area_triangulo(base,altura):
    a = (base * altura)/2
    return a

def area_rectangulo(base,altura):
    a = base * altura
    return a

def area_rombo(diagonal,diagonal2):
    a = (diagonal * diagonal2) / 2
    return a 

def area_circulo(radio):
    a = math.pi * radio**2
    return a