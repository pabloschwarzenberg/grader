import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=(math.pi)*(radio**2)#######PI
    return area

if __name__ == "__main__":
    acciones="""Calcular área de:
(1)Triángulo
(2)Rectanguro
(3)Rombo
(4)Círculo"""
    print(acciones)
    accion=int(input("¿Qué área desea calcular?:"))
    if accion==1:
        base=int(input("base:"))
        altura=int(impt("altura:"))
        area=area_triangulo(base,altura)
        print(area)           
    elif accion==2:
        base=int(input("base:"))
        altura=int(impt("altura:"))
        area=area_rectangulo(base,altura)
        print(area) 
    elif accion==3:
        diagonal1=int(input("diagonal1:"))
        diagonal2=int(input("diagonal2:"))
        area=area_rombo(diagonal1,diagonal2)
        print(area) 
    elif accion==4:
        radio=int(input("radio:"))
        area=area_circulo(radio)
        print(area)  