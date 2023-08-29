import math
def area_triangulo(base,altura):
    atria = (base*altura)/2
    return atria

def area_rectangulo(base,altura):
    arec = (base*altura)
    return arec

def area_rombo(diagonal1,diagonal2):
    aromb = (diagonal1*diagonal2)/2
    return aromb

def area_circulo(radio):
    acirc = float(pow(radio,2)*math.pi)
    return acirc
           