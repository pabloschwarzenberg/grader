import math

def area_triangulo(base,altura):
    base = int(base)
    altura = int(altura)
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    base = int(base)
    altura = int(altura)
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    diagonal1 = int(diagonal1)
    diagonal2 = int(diagonal2)
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    radio = int(radio)
    area = (math.pi)*(radio*radio)
    return area