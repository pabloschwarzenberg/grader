import math
def area_triangulo(base, altura):
    
    areat = (base * altura) / 2
    return areat
    pass

def area_rectangulo(base, altura):
    arear = (base * altura)
    return arear
    pass

def area_rombo(diagonal1, diagonal2):
    arearb = (diagonal1 * diagonal2) / 2
    return arearb
    pass

def area_circulo(radio):
    areac = math.pi * (radio ** 2)
    return areac
    pass
           