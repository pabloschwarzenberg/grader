import math

def area_triangulo(base,altura):
    a_triangulo=(base*altura)/2
    return a_triangulo

def area_rectangulo(base,altura):
    a_rectangulo=base*altura
    return a_rectangulo

def area_rombo(diagonal1,diagonal2):
    a_rombo=diagonal1*diagonal2/2
    return a_rombo

def area_circulo(radio):
    a_circulo=math.pi*radio**2
    return a_circulo
  