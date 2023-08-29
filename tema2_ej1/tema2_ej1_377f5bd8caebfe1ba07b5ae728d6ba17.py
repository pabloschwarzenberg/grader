import math
math.pi
def area_triangulo(base,altura):
    a=base*altura*0.5
    return a
def area_rectangulo(base,altura):
    a=base*altura
    return a
def area_rombo(diagonal1,diagonal2):
    a=diagonal1*diagonal2*0.5
    return a
def area_circulo(radio):
    a=math.pi*radio*radio
    return a
def menu():
    x=int(input("Ingrese una opcion numerica 1.Triangulo,2.Rectangulo,3.rombo,4.circulo:  "))
    if x==1:
        y=int(input("Ingrese base"))
        z=int(input("Ingrese altura"))
        q=area_triangulo(y,z)
        print(q)
    elif x==2:
        y=int(input("Ingrese base"))
        z=int(input("Ingrese altura"))
        q=area_rectangulo(y,z)
        print(q)
    elif x==3:
         y=int(input("Ingrese base"))
         z=int(input("Ingrese altura"))
         q=area_rombo(y,z)
         print(q)
    elif x==4:
         y=int(input("Ingrese Radio"))
         q=area_circulo(y)
         print(q)

           