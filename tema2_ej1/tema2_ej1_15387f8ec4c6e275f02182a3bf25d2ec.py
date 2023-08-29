import math
def area_triangulo(base,altura):
    p = (base * altura) / 2
    return(p)

def area_rectangulo(base,altura):
    p = (base*altura)
    return(p)

def area_rombo(diagonal_1,diagonal_2):
    p = (diagonal_1 * diagonal_2) / 2
    return(p)

def area_circulo(radio):
    p = math.pi * radio**2
    return(p)
           