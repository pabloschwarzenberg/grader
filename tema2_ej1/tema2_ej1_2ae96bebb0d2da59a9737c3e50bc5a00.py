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
    area = math.pi * radio ** 2
    return area

verdad = True
while verdad == True:
    if __name__ == "__main__":
        objeto = int(input("Area a calcular:\(1)Triangulo\(2)Rectangulo\(3)Rombo\(4)Circulo"))
        if objeto == 1:
            base = int(input("Base:"))
        altura = int(input("Altura:"))
        print(area_triangulo(base, altura))

        if objeto == 2:
            base = int(input("Base:"))
        Altura = int(input("Altura:"))
        print(area_rectangulo(base, altura))

        if objeto == 3:
            diagonal1 = int(input("Diagonal1:"))
        diagonal2 = int(input("Diagonal2:"))
        print(area_rombo(diagonal1, diagonal2))

        if objeto == 4:
            radio = int(input("Radio:"))
        print(area_circulo(radio))
    else:
        verdad = False
           