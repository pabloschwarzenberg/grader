import math


def area_triangulo(base, altura):
    result = base * altura / 2
    return result
    pass


def area_rectangulo(base, altura):
    resulta = base * altura
    return resulta
    pass


def area_rombo(diagonal1, diagonal2):
    resultad = diagonal1 * diagonal2 / 2
    return resultad
    pass


def area_circulo(radio):
    resultado = math.pi * radio**2
    return resultado
    pass


if __name__ == "__main__":
    a = input()
    if a == "area triangulo":
        b = int(input())
        c = int(input())
        print(area_triangulo(b, c))
    if a == "area rectangulo":
        d = int(input())
        e = int(input())
        print(area_rectangulo(d, e))
    if a == "area rombo":
        f = int(input())
        g = int(input())
        print(area_rombo(f, g))
    if a == "area circulo":
        roberto = int(input())
        print(area_circulo(roberto))
    pass


           