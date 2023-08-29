# Calculadora Geométrica
# 2 points
#
# Construye un programa que permita calcular el área de un rectángulo, un
# triángulo, un rombo y un círculo, creando una función específica para cada
# figura geométrica y con un menú que permita escoger lo que la persona desea
# calcular. (Importa desde la librería math, la constante pi).
#

import math

def area_triangulo(base,altura):
    return (base * altura) / 2

def area_rectangulo(base,altura):
    return base * altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2