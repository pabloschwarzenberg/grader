import math

def area_triangulo(base,altura):
    area_tria= (base*altura)/2
    return area_tria

def area_rectangulo(base,altura):
    area_rec=base*altura

    return area_rec

def area_rombo(diagonal1,diagonal2):
    area_rom=(diagonal1*diagonal2)/2
    return area_rom

def area_circulo(radio):
    pi=(math.pi)
    area_circ=pi*radio**2
    return area_circ
    if _name_ == "_main_":
     print("Escriba el numero de la opcion que desea usar:")
     print("Area de un triangulo----1")
     print("Area de un rectangulo----2")
     print("Area de un rombo----3")
     print("Area de un circulo----4")
     pregu=int(input(" "))
    if pregu==1:
        base=int(input("Ingrese base del triangulo"))
        altura=int(input("Ingrese altura del triangulo"))
        area=area_triangulo(base,altura)
        print(area) 
    elif pregu==2:
        base=int(input("Ingrese base del rectangulo"))
        altura=int(input("Ingrese altura del rectangulo"))
        area=area_rectangulo(base,altura)
        print(area) 
    elif pregu==3:
        d1=int(input("Ingrese diagonal 1 del rombo"))
        d2=int(input("Ingrese diagonal 2 del rombo"))
        area=area_rombo(d1,d2)
        print(area) 
    elif pregu==4:
        r=int(input("Ingrese radio del circulo"))
        area=area_circulo(r)
        print(area)
    