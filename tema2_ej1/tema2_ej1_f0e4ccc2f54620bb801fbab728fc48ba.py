import math
def area_triangulo(base,altura):
    AreaT = float((base*altura)/2)
    return AreaT

def area_rectangulo(base,altura):
    AreaRe = float(base*altura)
    return AreaRe

def area_rombo(diagonal1,diagonal2):
    AreaRo = float((diagonal1*diagonal2)/2)
    return AreaRo

def area_circulo(radio):
    AreaCi = float(math.pi*radio**2)
    return AreaCi           