import math
def area_triangulo(base,altura):
    a=(base*altura)/2
    return(a)
def area_rectangulo(base,altura):
    a=(base*altura)
    return(a)
def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return(a)
def area_circulo(radio):
    pi=math.pi
    a=pi*(radio**2)
    return(a)
if __name__ == "__main__":
    dc=("Modos:\n1-triangulo\n2-rectangulo\n3-rombo\n4-circulo")
    print(dc)
    modo=int(input("elige el modo:"))
    if modo==1:
        a=float(input("base: "))
        b=float(input("altura: "))
        c=area_triangulo(a,b)
        print("resultado:",c)
    if modo==2:
        a=float(input("base: "))
        b=float(input("altura: "))
        c=area_rectangulo(a,b)
        print("resultado:",c)
    if modo==3:
        a=float(input("diagonal1: "))
        b=float(input("diagonal2: "))
        c=area_rombo(a,b)
        print("resultado:",c)
    if modo==4:
        a=float(input("radio: "))
        c=area_circulo(a)
        print("resultado:",c)   