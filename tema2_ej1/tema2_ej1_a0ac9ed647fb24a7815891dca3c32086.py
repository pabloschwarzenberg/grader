import math

def menu():
    print("""Elija una opción
    1) Rectángulo
    2) Triángulo
    3) Rombo
    4) Círculo""")
    return ""


def area_triangulo(base,altura):
    area = (base * altura)/2
    return area


def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area

def area_circulo(radio):
    area = (radio**2)*math.pi
    return area
           