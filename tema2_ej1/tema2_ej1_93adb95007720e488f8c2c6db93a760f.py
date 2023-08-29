import math
pi = math.pi

def area_triangulo(base,altura):
    area = (base * altura)/2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    area = pi * (radio ** 2)
    return area

if __name__ == "__main__":
    elige = int(input("Eliga lo que quiere calcular: "))
    if elige == 1:
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        print(area_triangulo(base, altura))
    if elige == 2:
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        print(area_rectangulo(base, altura))
    if elige == 3:
        diagonal1 = int(input("Diagonal 1: "))
        diagonal2 = int(input("Diagonal 2: "))
        print(area_rombo(diagonal1, diagonal2))
    if elige == 4:
        radio = int(input("Radio: "))
        print(area_circulo(radio))

    