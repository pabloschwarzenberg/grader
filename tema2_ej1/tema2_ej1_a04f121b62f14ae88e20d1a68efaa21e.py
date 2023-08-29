import math
figura="Triangulo","Rectangulo","Rombo","Circulo"

def area_triangulo(base,altura):
    atri=(base*altura)/2
    return atri

def area_rectangulo(base,altura):
    arec=base*altura
    return arec

def area_rombo(diagonal1,diagonal2):
    arom=((diagonal1*diagonal2)/2)
    return arom

def area_circulo(radio):
    acir=(radio**2)*math.pi
    return acir

if figura==0:
    print("Escriba su base, luego la altura")
    area=area_triangulo(base,altura)
    print (int(area))
elif figura==1:
    print("Escriba su base, luego la altura")
    area=area_rectangulo(base,altura)
    print (int(area))
elif figura==2:
    print("Escriba el valor de la diagonal 1, luego la diagonal 2")
    area=area_rombo(diagonal1,diagonal2)
    print (int(area))
elif figura==3:
    print("Escriba el valor del radio")
    area=area_circulo(radio)
    print (int(area))
           