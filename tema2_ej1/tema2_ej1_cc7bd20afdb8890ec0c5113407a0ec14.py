from math import pi
def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=pi*radio*radio
    return area