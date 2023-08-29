from math import pi
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area2 = base*altura
    return area2

def area_rombo(diagonal1,diagonal2):
    ar3a = diagonal1*diagonal2/2
    return ar3a

def area_circulo(radio):
    arear = pi*(radio*radio)
    return arear