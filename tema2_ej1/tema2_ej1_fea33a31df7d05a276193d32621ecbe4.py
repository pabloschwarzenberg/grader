def area_triangulo(base,altura):
    Area=(base*altura)/2
    return Area

def area_rectangulo(base,altura):
    Area=base*altura
    return Area

def area_rombo(diagonal1,diagonal2):
    Area=(diagonal1*diagonal2)/2
    return Area

def area_circulo(radio):
    import math
    Area=(math.pi)*(radio**2)
    return Area
    
    

if __name__ =="_main_":
    N=int(inpur("¿que area desea saber 1(triangulo),2(rectangulo),3(rombo) o 4(circulo)?"))
    if N==1:
       b=int(input("Ingrese base: "))
       a=int(input("Ingrese altura: "))
       print(area_triangulo(b,a))
    if N==2:
       b=int(input("Ingrese base: "))
       a=int(input("Ingrese altura: "))
       print(area_rectangulo(b,a))
    if N==3:
       d1=int(input("Ingrese diagonal 1: "))
       d2=int(input("Ingrese diagonal 2: "))
       print(area_rombo(d1,d2))
    if N==3:
       r=int(input("Ingrese radio: "))
       print(area_circulo(r))    

    
           