import math

def area_triangulo(base,altura):
    resultado = (base*altura)/2
    return resultado

def area_rectangulo(base,altura):
    resultado = base*altura
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado = (diagonal1*diagonal2)/2
    return resultado

def area_circulo(radio):
    from math import pi
    resultado = pi*radio*radio
    float(resultado)
    return resultado