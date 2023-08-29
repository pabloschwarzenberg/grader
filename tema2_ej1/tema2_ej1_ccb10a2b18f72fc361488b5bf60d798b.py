from math import pi
def area_triangulo(base,altura):
    a= (base*altura)/2
    return a
def area_rectangulo(base,altura):
    a= base*altura
    return a
def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return a
def area_circulo(radio):
    a= (pi)*(radio**2)
    return a
def menu():
    f=1
    if f==1:
        base=2
        altura=4
        print(area_triangulo(base,altura))
    if f==2:
        b=int(input("ingrese la base:"))
        alt=int(input("ingrese altura:"))
        print(area_rectangulo(b,alt))
    if f==3:
        d1=int(input("ingrese la diagonal1:"))
        d2=int(input("ingrese diagonal2:"))
        print(area_rombo(d1,d2))
    if f==4:
        rad=int(input("ingrese radio:"))
        print(area_ciruclo(rad))
menu()
    
    

           