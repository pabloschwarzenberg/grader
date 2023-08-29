import math

def area_triangulo(base,altura):
    areaTRIANGULO = (base * altura) / 2
    return areaTRIANGULO

def area_rectangulo(base,altura):
    areaRECTANGULO = base * altura
    return areaRECTANGULO

def area_rombo(diagonal1,diagonal2):
    areaROMBO = (diagonal1 * diagonal2) / 2
    return areaROMBO

def area_circulo(radio):
    pi = math.pi
    areaCIRCULO = (radio ** 2) * pi
    return areaCIRCULO

    pass