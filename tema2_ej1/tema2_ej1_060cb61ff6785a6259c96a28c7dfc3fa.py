import math


def area_triangulo(base,altura):
    return base * altura / 2


def area_rectangulo(base,altura):
    return base * altura


def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 / 2


def area_circulo(radio, pi=math.pi):
    return pi * radio ** 2


if __name__ == "__main__":
    figura = input('Selecciona una figura: ').lower().strip()
    if figura == 'triangulo':
        base = int(input('Ingresa base: '))
        altura = int(input('Ingresa altura: '))
        print(area_triangulo(base, altura))
    elif figura == 'rectangulo':
        base = int(input('Ingresa base: '))
        altura = int(input('Ingresa altura: '))
        print(area_rectangulo(base, altura))
    elif figura == 'rombo':
        d1 = int(input('Ingresa diagonal 1: '))
        d2 = int(input('Ingresa diagonal 2: '))
        print(area_rombo(d1, d2))
    elif figura == 'circulo':
        r = int(input('Ingresa el radio del circulo: '))
        print(area_circulo(r))