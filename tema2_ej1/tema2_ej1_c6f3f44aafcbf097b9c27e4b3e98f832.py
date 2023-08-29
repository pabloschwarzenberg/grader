#calculadora

import math
def area_triangulo(base, alt):
    return base * alt/2
def area_rectangulo(base, alt):
    return base * alt
def area_rombo(diag1, diag2):
    return (diag1 * diag2)/2
def area_circulo(radio):
    return math.pi * radio ** 2