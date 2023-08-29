from math import *

def area_triangulo(base,altura):
    area=(base*altura)/2
    print(float(area))
    return area

def area_rectangulo(base,altura):
    area=(base*altura)
    print(float(area))
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    print(float(area))
    return area

def area_circulo(radio):
    area=pi*(radio**2)
    print(float(area))
    return area

if __name__ == "__main__":
    
    calc=int(input(" qué área deseas calcular? 1.-rectángulo, 2.- triángulo, 3.- rombo, 4.- círculo"))

    if calc==1:
        base=int(input("ingresa la base del rectángulo:"))
        altura=int(input("ingresa la altura del rectángulo:"))
        area_triangulo(base,altura)
        

    elif calc==2:
        base=int(input("ingresa la base del triangulo:"))
        altura=int(input("ingresa la altura del triangulo:"))
        area_rectangulo(base,altura)

    elif calc==3:
        diagonal1=int(input("ingresa la diagonal 1 del rombo:"))
        diagonal2=int(input("ingresa la diagonal 2 del rombo:"))
        area_rombo(diagonal1,diagonal2)

    elif calc==4:
        radio=int(input("ingresa el radio del círculo:"))
        area_circulo(radio)


    