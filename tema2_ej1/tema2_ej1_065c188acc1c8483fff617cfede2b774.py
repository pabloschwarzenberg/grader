import math

def area_rectangulo(lado, alto):
    area = lado * alto
    return area

def area_triangulo(lado, alto):
    area = (lado * alto) / 2
    return area

def area_rombo(lado, alto):
    area = lado * alto / 2
    return area

def area_circulo(radio):
    area = math.pi * (radio**2)
    return area
