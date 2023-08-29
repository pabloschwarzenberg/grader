from math import pi
def area_triangulo(base,altura):
    a=(base*altura)/2
    return a

def area_rectangulo(base,altura):
    a=(base*altura)
    return a

def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return a
def area_circulo(radio):
    a=(pi)*(radio**2)
    return a
def menu():
    f=1

    if f==1:
        base=2
        altura=4
        print(area_triangulo(base,altura))
    if f==2:
        b=int(input("Ingrese la base: "))
        alt=int(input("Ingrese altura: "))
        print(area_rectangulo(b,alt))
    if f==3:
        d1=int(input("Ingrese la diagonal1: "))
        d2=int(input("Ingrese la diagonal2: "))
        print(area_rombo(d1,d2))
    if f==4:
        rad=int(input("Ingrese radio: "))
        print(area_circulo(rad))
menu()