import math
def area_triangulo(base,altura):
    resultado=(base*altura/2)
    return resultado 

def area_rectangulo(base,altura):
    resultado=(base*altura)
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado=(diagonal1*diagonal2/2)
    return resultado

def area_circulo(radio):
    resultado=(math.pi*radio**2)
    return resultado
           