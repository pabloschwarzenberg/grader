import math

def area_triangulo(base,altura):
    result = (base * altura) / 2
    return result

def area_rectangulo(base,altura):
    result = base * altura
    return result

def area_rombo(diagonal1,diagonal2):
    result = (diagonal1 * diagonal2) / 2
    return result

def area_circulo(radio):
    result = math.pi * radio**2
    return result