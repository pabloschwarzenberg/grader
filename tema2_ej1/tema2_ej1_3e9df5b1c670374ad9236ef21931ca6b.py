def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area_rec = base*altura
    return area_rec


def area_rombo(diagonal1,diagonal2):
    rombo = (diagonal1*diagonal2)/2
    return rombo

def area_circulo(radio):
    from math import pi
    area_circ = pi*(radio**2)
    return area_circ

           