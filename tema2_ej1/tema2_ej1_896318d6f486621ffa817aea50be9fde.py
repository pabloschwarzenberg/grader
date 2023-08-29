from math import pi
def area_triangulo(base, altura):
    area_total = base*altura / 2
    return area_total


def area_rectangulo(base, altura):
    area_total = base*altura
    return area_total


def area_circulo(radio):
    area_total = pi * radio ** 2
    return area_total


def area_rombo(diagonal1, diagonal2):
    area_total = diagonal1 * diagonal2 / 2
    return area_total