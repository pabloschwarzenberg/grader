import math
import sys
def area_triangulo(base,altura):
    a=(base*altura)/2
    return a
def area_rectangulo(base,altura):
    b=base*altura
    return b
def area_rombo(diagonal1,diagonal2):
    c=(diagonal1*diagonal2)/2
    return c
def area_circulo(radio):
    d=(math.pi*(radio**2))
    return d
if __name__=="__main__":
    eleccion=int(input("la figura a calcular es 1)triangulo, 2)rectangulo, 3)rombo o 4)circulo: "))
    if eleccion==1:
        base=int(input("ingresa base: "))
        altura=int(input("ingresa altura: "))
        print(area_triangulo(base,altura))
    elif eleccion==2:
        base=int(input("ingresa base: "))
        altura=int(input("ingresa altura: "))
        print(area_rectangulo(base,altura))
    elif eleccion==3:
        diagonal1=int(input("ingresa medida de la diagonal 1: "))
        diagonal2=int(input("ingresa medida de la diagonal 2: "))
        print(area_rombo(diagonal1,diagonal2))
    elif eleccion==4:
        radio=int(input("ingresa el radio del circulo: "))
        print(area_circulo(radio))
    else:
        sys.exit(1)