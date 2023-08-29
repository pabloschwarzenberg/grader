from math import pi

def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(area)
    return area
    pass


def area_rectangulo(base, altura):
    area = base * altura
    print(area)
    return area
    pass


def area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    print(area)
    return area
    pass


def area_circulo(radio):
    area = pi * radio ** 2
    print(area)
    return area
    pass
 
 