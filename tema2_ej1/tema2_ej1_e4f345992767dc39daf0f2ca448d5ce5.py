import math
def area_triangulo(b,h):
    a = b * h/2
    return a
    
def area_rectangulo(b,h):
    a = b * h
    return a

def area_rombo(diagonal1,diagonal2):
    a = (diagonal1*diagonal2)/2
    return a

def area_circulo(r):
    a = math.pi*r**2
    return a   