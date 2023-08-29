from math import pi

def area_triangulo(base, altura):
    return (base * altura / 2)

def area_rectangulo(base, altura):
    return (base * altura)


def area_rombo(diagonal1, diagonal2):
    return (diagonal1*diagonal2/2)


def area_circulo(radio):
    return (pi * radio**2)


if __name__ == "__main__":
    base = float(input())
    altura = float(input())
    diagonal1 = float(input())
    diagonal2 = float(input())
    radio = float(input())
    print(area_triangulo(base, altura))
    print(area_rectangulo(base, altura))
    print(area_rombo(diagonal1, diagonal2))
    print(area_circulo(radio))


