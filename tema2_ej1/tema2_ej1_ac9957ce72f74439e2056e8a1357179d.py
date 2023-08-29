from math import pi


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_rectangulo(base, altura):
    return base * altura


def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2


def area_circulo(radio):
    return (radio ** 2) * pi


if __name__ == "__main__":
    chosen = input("Area a calcular: ")
    if chosen == "triangulo":
        print(area_triangulo(eval(input("base: ")), eval(input("altura: "))))
    elif chosen == "rectangulo":
        print(area_rectangulo(eval(input("base: ")), eval(input("altura: "))))
    elif chosen == "rombo":
        print(area_rombo(eval(input("diagonal1: ")), eval(input("diagonal2: "))))
    elif chosen == "circulo":
        print(area_circulo(eval(input("radio: "))))
    pass
     