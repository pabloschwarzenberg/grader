import math
def area_triangulo(base, altura):
    areaTriangulo = (base * altura)/2
    return areaTriangulo
    pass


def area_rectangulo(base, altura):
    areaRectangulo = (base * altura)
    return areaRectangulo
    pass


def area_rombo(diagonal1, diagonal2):
    areaRombo = (diagonal1 * diagonal2)/2
    return areaRombo
    pass


def area_circulo(radio):
    areaCirculo = (math.pi * (radio * radio))
    return areaCirculo
    pass
