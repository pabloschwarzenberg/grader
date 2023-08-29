import math

def area_triangulo(base,altura):
    solucion = (base * altura)/2
    return solucion

def area_rectangulo(base,altura):
    solucion = (base * altura)
    return solucion

def area_rombo(diagonal1,diagonal2):
    solucion = (diagonal1 * diagonal2)/2
    return solucion

def area_circulo(radio):
    solucion = ((math.pi) * (radio ** 2))
    return solucion

