def area_triangulo(base, altura):
    areaTriangulo = (base * altura) / 2
    return areaTriangulo


def area_rectangulo(base, altura):
    areaRectangulo=base*altura
    return areaRectangulo



def area_rombo(diagonal1, diagonal2):
    areaRombo=(diagonal1*diagonal2)/2
    return areaRombo



def area_circulo(radio):
    from math import pi
    areaCirculo=pi*(radio**2)
    return areaCirculo