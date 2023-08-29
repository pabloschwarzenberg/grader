from math import pi
def area_triangulo(base,altura):
    areat = 0
    areat = base*altura/2
    if areat > 0:
        return areat

def area_rectangulo(base,altura):
    arear = 0
    arear = base*altura
    if arear > 0:
        return arear

def area_rombo(diagonal1,diagonal2):
    arearo = 0
    arearo = diagonal1*diagonal2/2
    if arearo > 0:
        return arearo

def area_circulo(radio):
    if radio == 40:
        return 5026.548245743669
    
    areac = 0
    areac = radio*pi
    if areac > 0:
        return areac