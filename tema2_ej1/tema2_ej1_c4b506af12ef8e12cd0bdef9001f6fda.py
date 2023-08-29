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
    area=math.pi*radio^2
    return area


print("Bienvenido a nuestra calculadora de areas, ¿que area desea calcular?")
seleccion=int(input("1.-Área Triangulo\n2.-Área Rectangulo\n3.-Área Rombo\n4.-Área Circulo\nIngrese opcion: "))
if seleccion==1:
    base=int(input("Ingrese base del triangulo: "))
    altura=int(input("Ingrese altura del triangulo: "))
    area=area_triangulo(base,altura)
    print("El area del triangulo es: ",area)
elif seleccion==2:
    base=int(input("Ingrese base del rectangulo: "))
    altura=int(input("Ingrese altura del rectangulo: "))
    area=area_rectangulo(base,altura)
    print("El area del rectanguloo es: ",area)
elif seleccion==3:
    diagonal1=int(input("Ingrese primera diagonal del rombo: "))
    diagonal2=int(input("Ingrese segunda diagonal del rombo: "))
    area=area_rombo(diagonal1,diagonal2)
    print("El area del rombo es: ",area)
elif seleccion==4:
    radio=int(input("Ingrese radio del circulo: "))
    area=area_circulo(radio)
    print("El area del circulo es: ",area)