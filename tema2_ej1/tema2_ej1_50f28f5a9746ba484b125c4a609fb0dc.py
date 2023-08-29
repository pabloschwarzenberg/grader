import math

def area_triangulo(base,altura):
    atri=(base*altura)/2
    return atri

def area_rectangulo(base,altura):
    arec=base*altura
    return arec

def area_rombo(diagonal1,diagonal2):
    arom=(diagonal1*diagonal2)/2
    return arom

def area_circulo(radio):
    acir=math.pi*(radio**2)
    return acir
    
if __name__ == "__main__":
    pass
           