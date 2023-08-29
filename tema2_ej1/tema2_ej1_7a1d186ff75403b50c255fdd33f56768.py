import math
def area_triangulo(base,altura):
    Triangulo = (base*altura)/2
    return Triangulo 

def area_rectangulo(base,altura):
    Rectangulo = base*altura
    return Rectangulo

def area_rombo(diagonal1,diagonal2):
    Rombo = (diagonal1*diagonal2)/2
    return Rombo

def area_circulo(radio):
    Circulo = radio**2*math.pi
    return Circulo