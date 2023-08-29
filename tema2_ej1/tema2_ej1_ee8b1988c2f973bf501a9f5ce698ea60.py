import math

# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el área de un rombo
def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2

