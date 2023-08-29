import math


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


def area_rectangulo(base, altura):
    area = base * altura
    return area


def area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area


def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area


if __name__ == "__main__":
    if area_rectangulo():
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))

    elif area_triangulo():
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))

    elif area_rombo():
        diagonal1 = int(input("Ingrese la diagonal 1: "))
        diagonal2 = int(input("Ingrese la diagonal 2: "))

    elif area_circulo():
        radio = int(input("Ingrese el radio: "))