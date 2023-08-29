import math
def area_triangulo(base,altura):
    area=base*altura/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=(math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    print("Esto calcula el área de figuras geométricas")
    print("(1) Triángulo")
    print("(2) Rectángulo")
    print("(3) Rombo")
    print("(4) Círculo")
    f=int(input("¿A qué figura le debes calcular el área?: "))
    if f==1:
        b=int(input("Ingrese la base del triángulo: "))
        h=int(input("Ingrese la altura del triánguglo: "))
        a=area_triangulo(b,h)
        print("El área del triángulo es {0}".format(a))
    if f==2:
        b=int(input("Ingrese la base del rectángulo: "))
        h=int(input("Ingrese la altura de rectángulo: "))
        a=area_rectangulo(b,h)
        print("El área del rectángulo es {0}".format(a))
    if f==3:
        d1=int(input("Ingrese la diagonal 1 del rombo: "))
        d2=int(input("Ingrese la diagonal 2 del rombo: "))
        a=area_rombo(d1,d2)
        print("El área del rombo es {0}".format(a))
    if f==4:
        r=int(input("Ingrese el radio del círculo: "))
        a=area_circulo(r)
        print("El área del círculo es {0}".format(a))

           