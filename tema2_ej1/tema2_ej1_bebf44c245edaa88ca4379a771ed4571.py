import math

def area_triangulo(base,altura):
    atr=base*altura/2
    return atr

def area_rectangulo(base,altura):
    are=base*altura
    return are

def area_rombo(diagonal1,diagonal2):
    aro=diagonal1*diagonal2/2
    return aro

def area_circulo(radio):
    aci=math.pi*radio*radio
    return aci

if __name__ == "__main__":
    print(atr, are, aro, aci)
           