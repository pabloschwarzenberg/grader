import math
def area_triangulo(base,altura):
    t=(base*altura)/2
    return t

def area_rectangulo(base,altura):
    r=base*altura
    return r

def area_rombo(diagonal1,diagonal2):
    ro=(diagonal1*diagonal2)/2
    return ro

def area_circulo(radio):
    c=math.pi*radio*radio
    return c
areas=["triangulo", "rectangulo", "rombo", "circulo"]

if __name__ == "__main__":
    a=int(input("""Escoja el area que desee calcular, eligiendo un numero del 0 al 3
    (0)triangulo
    (1)rectangulo
    (2)rombo
    (3)circulo
    Area:"""))
    if a==0:
        base=int(input("Ingrese la base:"))
        altura=int(input("Ingrese la altura:"))
        print(area_triangulo(base,altura))
    elif a==1:
        base=int(input("Ingrese la base:"))
        altura=int(input("Ingrese la altura:"))
        print(area_rectangulo(base,altura))
    elif a==2:
        diagonal1=int(input("Ingrese la diagonal1:"))
        diagonal2=int(input("Ingrese la diagonal 2:"))
        print(area_romba(diagonal1,diagonal2))
    elif a==3:
        radio=int(input("Ingrese el radio:"))
        print(area_circulo(radio))
           