import math

def area_triangulo(base, altura):
    at = (base*altura)/2
    return at
def area_rectangulo(base, altura):
    arec = base*altura
    return arec
def area_rombo(diagonal1, diagonal2):
    arom = (diagonal1*diagonal2)/2
    return arom
def area_circulo(radio):
    ac = math.pi*(radio**2)
    return ac


