import math
pi = math.pi

def area_triangulo(base,altura):
    formula = (base*altura)/2
    return formula

def area_rectangulo(base,altura):
    formula = base*altura
    return formula

def area_rombo(diagonal1,diagonal2):
    formula = (diagonal1*diagonal2)/2
    return formula

def area_circulo(radio):
    formula = pi*(radio**2)
    return formula 