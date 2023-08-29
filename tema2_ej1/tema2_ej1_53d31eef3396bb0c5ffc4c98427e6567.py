import math
from math import pi
def area_triangulo(base,altura):
    at=(base*altura)/2
    return at
    pass

def area_rectangulo(base,altura):
    ar=(base*altura)
    return ar
    pass

def area_rombo(diagonal1,diagonal2):
    aro=(diagonal1*diagonal2)/2
    return aro
    pass

def area_circulo(radio):
    ac=pi*(radio**2)
    return ac 
    pass

if __name__ == "__main__":
    figura=input()
    if figura == triangulo:
        base=input()
        altura=input()