from math import pi

def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    return pi*(radio**2)

figuras={0:'triángulo',1:'rectángulo',2:'rombo',3:'círculo'}

if __name__ == "__main__":
    print("""0: Triángulo
1: Rectángulo
2: Rombo
3: Círculo""")
    numfig=int(input("Ingrese el número correspondiente a la figura cuya área desea calcular: "))
    if numfig==0:
        b=float(input("Base: "))
        h=float(input("Altura: "))
        res=area_triangulo(b,h)
    elif numfig==1:
        a=float(input("Ancho: "))
        b=float(input("Alto: "))
        res=area_rectangulo(a,b)
    elif numfig==2:
        d1=float(input("Diagonal 1: "))
        d2=float(input("Diagonal 2: "))
        res=area_rombo(d1,d2)
    elif numfig==3:
        r=float(input("Radio: "))
        res=area_circulo(r)
    print("El área de su {0} es {1}".format(figuras[numfig],res))
           