import math

def area_triangulo(base,altura):
    a = (base * altura) / 2
    return a
    
def area_rectangulo(base,altura):
    b = base * altura
    return b

def area_rombo(diagonal1,diagonal2):
    c = (diagonal1 * diagonal2) / 2
    return c

def area_circulo(radio):
    d = math.pi * (radio ** 2)
    return d