import math 

def area_triangulo(base,altura):
    areat=(base*altura)/2
    return areat

def area_rectangulo(base,altura):
    areart=base*altura
    return areart

def area_rombo(diagonal1,diagonal2):
    arearb=(diagonal1*diagonal2)/2
    return arearb

def area_circulo(radio):
    areac=math.pi*(radio**2)
    return areac