# CALCULADORA GEOMÉTRICA
import math

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_triangulo(base,altura):
    area =(base*altura)/2
    return area

def area_rombo(diagonalmayor,diagonalmenor):
    area = (diagonalmayor*diagonalmenor)/2
    return area

def area_circulo(radio):
    area = (radio**2)*math.pi
    return area