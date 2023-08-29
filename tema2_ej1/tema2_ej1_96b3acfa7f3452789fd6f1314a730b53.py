from math import pi

def area_triangulo(ba,al):
    r=(ba * al)/2 
    pass
    return r

def area_rectangulo(ba,al):
    r=ba * al
    pass
    return r

def area_rombo(di1,di2):
    r=(di1 * di2)/2
    pass
    return r

def area_circulo(ra):
    re=pi*(ra**2)
    pass
    return re

    a = input("figura: ")
    a.lower()
    if a == "triangulo":
        ba = int(input("ingrese la base: "))
        al = int(input("ingrese la altura: "))
        re = area_triangulo(ba, al)
        print(r)
    elif a == "rectangulo":
        ba = int(input("ingrese la base: "))
        al = int(input("ingrese la altura: "))
        re =  area_rectangulo(ba, al)
        print(r)
    elif a == "rombo":
        di1 = int(input("ingrese valor de la diagonal mayor: "))
        di2 = int(input("ingrese valor de la diagonal menor: "))
        re = area_rombo(di1, di2)
        print(r)
    elif a == "circulo":
        ra = int(input("ingrese el valor del radio: "))
        re = area_circulo(ra)
        print(r)
    pass