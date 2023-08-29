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
    from math import pi
    area = pi * radio**2 
    return area
           