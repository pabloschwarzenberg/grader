import math
def area_triangulo(base,altura):
    triangulo=base*altura/2
    return triangulo
    
def area_rectangulo(base,altura):
    rectangulo=base*altura
    return rectangulo

def area_rombo(diagonal1,diagonal2):
    rombo=diagonal1*diagonal2/2
    return rombo

def area_circulo(radio):
    circulo=math.pi*radio**2
    return circulo

if __name__ == "__main__":
    k=int(input("Ingrese el número de las siguientes funciones que desea realizar:\n1)area_triangulo\n2)area_rectangulo\n3)area_rombo\n4)area_circulo\n"))
    if k==1:
        base=int(input("Ingrese la base: "))
        altura=int(input("Ingrese la altura: "))
        print(area_triangulo(base,altura))
    elif k==2:
        base=int(input("Ingrese la base: "))
        altura=int(input("Ingrese la altura: "))
        print(area_rectangulo(base,altura))
    elif k==3:
        base=int(input("Ingrese la diagonal 1: "))
        altura=int(input("Ingrese la diagonal 2: "))
        print(area_rombo(base,altura))
    elif k==4:
        base=int(input("Ingrese el radio: "))
        print(area_circulo(base))

           