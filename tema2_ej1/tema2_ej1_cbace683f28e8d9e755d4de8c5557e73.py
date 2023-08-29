import math
def area_triangulo(base,altura):
    areatri = (base*altura)/2
    return areatri
def area_rectangulo(base,altura):
    arearec = (base*altura)
    return arearec
def area_rombo(diagonal1,diagonal2):
    arearomb = (diagonal1*diagonal2)/2
    return arearomb
def area_circulo(radio):
    areacirc = float(pow(radio,2)*math.pi)
    return areacirc
