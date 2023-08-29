import math

def area_triangulo(base,altura):
    Area_Triangulo = base * altura / 2
    return Area_Triangulo

def area_rectangulo(base,altura):
    Area_Rectangulo = base * altura
    return Area_Rectangulo

def area_rombo(diagonal1,diagonal2):
    Multiplicacion_diagonales = diagonal1 * diagonal2
    Area_Rombo = Multiplicacion_diagonales / 2
    return Area_Rombo

def area_circulo(radio):
     
    Radios = radio * radio
    Area__Circulo = math.pi * Radios
    return Area__Circulo
           