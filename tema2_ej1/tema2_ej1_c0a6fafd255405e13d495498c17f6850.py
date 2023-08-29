import math


def area_triangulo(bs, alt):
    return bs * alt / 2


def area_rectangulo(bs, alt):
    return bs * alt


def area_rombo(dnal1, dnal2):
    return (dnal1 * dnal2) / 2


def area_circulo(r):
    return math.pi * r ** 2