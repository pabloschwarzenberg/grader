def area_triangulo(base, altura):
    area_tri = (base*altura)/2
    return area_tri

def area_rectangulo(base_r, altura_r):
    area_re = (base_r*altura_r)
    return area_re

def area_rombo(diagonal_1, diagonal_2):
    area_rombo = (diagonal_1 * diagonal_2) /2
    return area_rombo

def area_circulo(radio):
    from math import pi
    area_cir = pi*radio**2
    return area_cir
