from math import *

def area_triangulo(base,altura):
    resultado = (base*altura)/2
    return resultado

def area_rectangulo(base,altura):
    resultado = base*altura
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado = (diagonal1*diagonal2)/2
    return resultado

def area_circulo(radio):
    resultado = pi*radio**2
    return resultado

if __name__ == "__main__":
    print("1 - para el area del triangulo\n2 - para el area del rectangulo\n3 - para area del rombo\n4 - para area del circulo")
    n = int(input("-: "))
    if(n == 1):
        base = int(input("Ingrese la base : "))
        altu = int(input("Ingrese la altura : "))
        print(area_triangulo(base,altu))
    elif(n == 2):
        base = int(input("Ingrese la base : "))
        altu = int(input("Ingrese la altura : "))
        print(area_rectangulo(base,altu))
    elif(n == 3):
        diago1 = int(input("Ingrese la diagonal 1 : "))
        diago2 = int(input("Ingrese la diagonal 2 : "))
        print(area_rombo(diago1,diago2))
    elif(n == 4):
        radio = int(input("Ingrese el radio: "))
        print(area_circulo(radio))
    else:
        print("error")
