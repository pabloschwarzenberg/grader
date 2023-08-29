import math

def area_triangulo(base, altura):
    area = ((base * altura)/2)


    return area


def area_rectangulo(base, altura):
    area = (base * altura)

    return area


def area_rombo(diagonal1, diagonal2):
    area = ((diagonal1 * diagonal2)/2)

    return area


def area_circulo(radio):
    area = (math.pi * (radio * radio))

    return area


if __name__ == "__main__":

    i = int(input("calculadora geometrica _____ 1 - triangulo ____ 2 - rectangulo _______ 3 - rombo _______ 4 - circulo : "))

    if i == 1:
        b = int(input("base : "))
        a =  int(input("altura : "))
        area_triangulo(b,a)
    if i == 2:
        b = int(input("base : "))
        a = int(input("altura : "))
        area_rectangulo(b, a)
    if i == 3:
        b = int(input("diagonal 1 : "))
        a = int(input("diagonal 2 : "))
        area_rombo(b, a)
    if i == 4:
        b = int(input("radio: "))
        area_circulo(b)