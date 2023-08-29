from cmath import pi


def area_triangulo(base,altura):
    A = (base*altura)/2
    return A

def area_rectangulo(base,altura):
    A = base*altura
    return A

def area_rombo(diagonal1,diagonal2):
    A = (diagonal1* diagonal2)/2
    return A

def area_circulo(radio):
    A = pi*(radio**2)
    return A 