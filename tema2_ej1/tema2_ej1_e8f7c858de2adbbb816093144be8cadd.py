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
        print(area_triangulo(base,altura))
    elif figura == rombo:
        diagonal1=input()
        diagonal2=input()
        print(area_rombo(diagonal1,diagonal2))
    elif figura==rectangulo:
        base=input()
        altura=input()
        print(area_rectangulo(base,altura))
    else:
        radio=input()
        print(area_circulo(radio))
    pass
           