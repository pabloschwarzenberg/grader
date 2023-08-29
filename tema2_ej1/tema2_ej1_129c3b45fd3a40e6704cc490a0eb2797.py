from math import pi
def area_triangulo(base, altura):
    r = (base * altura)/2
    return r


def area_rectangulo(base, altura):
    r = base * altura
    return r


def area_rombo(diagonal1, diagonal2):
    r = (diagonal1 * diagonal2) / 2
    return r


def area_circulo(radio):
    r = pi * (radio ** 2)
    return r