def area_triangulo(base, altura):
    area_tri = (base*altura)/2
    return area_tri


def area_rectangulo(base, altura):
    area_rec = (base*altura)
    return area_rec

def area_rombo(diagonal1, diagonal2):
    area_rom = (diagonal1*diagonal2)/2
    return area_rom

def area_circulo(radio):
    from math import pi
    area_cir = pi*(radio*radio)
    return area_cir