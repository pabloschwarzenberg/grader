import math
def area_triangulo(base,altura):
    A = (base*altura)/2
    return A

def area_rectangulo(base,altura):
    A2 = base*altura
    return A2

def area_rombo(diagonal1,diagonal2):
    A3 = (diagonal1*diagonal2)/2
    return A3
def area_circulo(radio):
    pi = math.pi
    A4 = pi * radio **2
    return A4