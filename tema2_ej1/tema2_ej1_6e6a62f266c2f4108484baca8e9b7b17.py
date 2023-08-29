import math
def area_triangulo(base,altura):
    areatri=base*altura/2
    return areatri

def area_rectangulo(base,altura):
    arearec=base*altura
    return arearec

def area_rombo(diagonal1,diagonal2):
    area_rombo=diagonal1*diagonal2/2
    return area_rombo
def area_circulo(radio):
    areacir= math.pi*radio**2
    return areacir           