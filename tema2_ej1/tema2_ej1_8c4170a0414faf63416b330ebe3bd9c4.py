#ENTRADA

import math
def area_rectangulo(b,h):
    a = h * b
    return a
    
#PROCESAMIENTO
    
def area_triangulo(b,h):
    a = h/2 * b
    return a

def area_circulo(r):
    a = math.pi * r ** 2
    return a
    
#SALIDA

def area_rombo(diag1,diag2):
    a = (diag2*diag1)/2
    return a

