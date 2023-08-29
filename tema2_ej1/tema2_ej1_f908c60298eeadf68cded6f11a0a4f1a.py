import math

def area_triangulo(Base,Altura):
    ar = (Base * Altura)/2
    return ar
def area_rectangulo(Base,Altura):
    ar = (Base * Altura)
    return ar

def area_rombo(Diagonal1,Diagonal2):
    ar = (Diagonal1 * Diagonal2)/2
    return ar

def area_circulo(radio):
    ar = math.pi * (radio ** 2)
    return ar
           