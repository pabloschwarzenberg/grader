import math
def area_triangulo(h,b):
    AT=h*b/2
    return AT
def area_rectangulo(b,h):
    AR=h*b
    return AR
def area_rombo(d1,d2):
    Ar=d1*d2/2
    return Ar
def area_circulo(r):
    AC=(math.pi)*r**2
    return AC
if __name__ == "__main__":
    qd=int(input("triangulo(1)\nrectangulo(2)\nrombo(3)\nCirculo(4)\nQue figura desea calcular?"))
    if qd==1:
        b=int(input("base triangulo:"))
        h=int(input("altura triangulo:"))
        print("Area=",area_triangulo(h,b))
    if qd==2:
        b=int(input("Ancho:"))
        h=int(input("Largo:"))
        print("Area=",area_rectangulo(b,h))
    if qd==3:
        d1=int(input("Diagonal 1:"))
        d2=int(input("Diagonal 2:"))
        print("Area=",area_rombo(d1,d2))
    if qd==4:
        r=int(input("Radio circulo:"))
        print("Area=",area_circulo(r))