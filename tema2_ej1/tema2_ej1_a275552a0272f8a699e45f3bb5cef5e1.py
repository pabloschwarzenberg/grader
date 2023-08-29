import math
def area_triangulo(base,altura):
    areatri=(base*altura)/2
    return areatri

def area_rectangulo(base,altura):
    arearect=base*altura
    return arearect

def area_rombo(diagonal1,diagonal2):
    arearo=(diagonal1*diagonal2)/2
    return arearo

def area_circulo(radio):
    areacirc=math.pi*((radio)**2)
    return areacirc
