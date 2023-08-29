from math import pi
import time

def area_triangulo(h,base):
    area= (base*h)/2
    return area

def area_rectangulo(a,b):
    area= a*b
    return area

def area_rombo (diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area= pi*(radio**2)
    return area
