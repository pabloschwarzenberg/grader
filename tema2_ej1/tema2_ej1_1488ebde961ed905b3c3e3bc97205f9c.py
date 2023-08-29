import math


def area_triangulo(Base, altura):
    return Base * altura/2
    
def area_rectangulo(Base, altura):
    return Base * altura


def area_rombo(diagonaL1, diagonaL2):
    return (diagonaL1 * diagonaL2) / 2


def area_circulo(radio):
    return math.pi * radio ** 2
           