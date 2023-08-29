from math import pi
def area_triangulo(base,altura):
    resultado_t = (base * altura)/2
    return resultado_t

def area_rectangulo(base,altura):
    resultado_r = base * altura
    return resultado_r

def area_rombo(diagonal1,diagonal2):
    resultado_r = (diagonal1 * diagonal2)/2
    return resultado_r

def area_circulo(radio):
    resultado_c = pi * radio**2
    return resultado_c 