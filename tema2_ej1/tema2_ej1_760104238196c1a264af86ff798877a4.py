import math
def area_triangulo(base, altura):
    return 0.5 * base * altura


def area_rectangulo(base, altura):
    return base * altura


def area_rombo(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2


def area_circulo(radio):
    pi = math.pi
    return pi * radio ** 2


if __name__ == "__main__":
    pass
