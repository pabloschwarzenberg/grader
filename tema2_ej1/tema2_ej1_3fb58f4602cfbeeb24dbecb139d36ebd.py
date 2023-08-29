import math
def area_triangulo(base,altura):
    areat=(base*altura)/2
    return areat
    pass

def area_rectangulo(base,altura):
    arear=base*altura
    return arear
    pass

def area_rombo(diagonal1,diagonal2):
    arearo=(diagonal1*diagonal2)/2
    return arearo
    pass

def area_circulo(radio):
    areac=radio**2*math.pi
    return areac
    pass

if __name__ == "__main__":
    baset=int(input())
    alturat=int(input())
    base=int(input())
    altura=int(input())
    diagonal1=int(input())
    diagonal2=int(input())
    radio=int(input())
    pass
           