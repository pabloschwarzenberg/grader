import math

def area_triangulo (base, altura):
    at=(base*altura)/2
    return at

def area_rectangulo (lado1,lado2):
    ar=(lado1*lado2)
    return ar

def area_rombo (diag1,diag2):
    aro=(diag2*diag1)/2
    return aro

def area_circulo (radio):
    ac=math.pi*(radio**2)
    return ac
