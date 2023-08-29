import math


def area_triangulo(b, a):
    t = (a * b) / 2
    return t
    pass


def area_rectangulo(b, a):
    rec = a * b
    return rec
    pass


def area_rombo(d1, d2):
    rom = (d1 * d2) / 2
    return rom
    pass


def area_circulo(r):
    c = math.pi*(r**2)
    return c
    pass


if __name__ == "__main__":
    triangulo=True
    rectangulo=True
    rombo=True
    circulo=True
    print("¿Qué área desea calcular?")
    figura = input()
    if figura == triangulo:
        b = int(input("Ingrese base: "))
        a = int(input("Ingrese altura: "))
        area_triangulo(b,a)
    elif figura == rectangulo:
        b = int(input("Ingrese base: "))
        a = int(input("Ingrese altura: "))
        area_rectangulo(b,a)
    elif figura == rombo:
        d1 = int(input("Ingrese diagonal 1: "))
        d2 = int(input("Ingrese diagonal 2:"))
        area_rombo(d1,d2)
    elif figura == circulo:
        r = int(input("Ingrese radio: "))
        area_circulo(r)
        pass
           

           