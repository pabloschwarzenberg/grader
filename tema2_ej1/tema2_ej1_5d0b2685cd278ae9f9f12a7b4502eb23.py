from math import pi
def area_triangulo(base,altura):
    base=int(base)
    altura=int(altura)
    area_t=base*altura/2
    pass
    return area_t

def area_rectangulo(base,altura):
    base=int(base)
    altura=int(altura)
    area_re=base*altura
    pass
    return area_re

def area_rombo(diagonal1,diagonal2):
    diagonal1=int(diagonal1)
    diagonal2=int(diagonal2)
    area_ro=diagonal1*diagonal2/2
    pass
    return area_ro

def area_circulo(radio):
    radio=int(radio)
    area_c=pi*radio*radio
    pass
    return area_c

if __name__ == "__main__":
    pass
           