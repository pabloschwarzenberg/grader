__author__ = 'Damian'
import math
def area_triangulo(base,altura):
    A=base*altura/2
    return A
def area_rectangulo(base,altura):
    A=base*altura
    return A
def area_rombo(d1,d2):
    A=d1*d2/2
    return A
def area_circulo(radio):
    A=math.pi*radio*radio
    return A

print("Las figuras disponibles para calcular el area son:")
print("[1]Triangulo")
print("[2]Rectangulo")
print("[3]Rombo")
print("[4]Circulo")
if __name__ == "__main__":
    figura=int(input("Ingrese el numero de la figura que desea:"))
    if figura==1:
        b=float(input("Ingrese el largo de la base:"))
        a=float(input("Ingrese la altura:"))
        area=area_triangulo(b,a)
    elif figura==2:
        b=float(input("Ingrese el largo de la base:"))
        a=float(input("Ingrese la altura:"))
        area=area_rectangulo(b,a)
    elif figura==3:
        a=float(input("Ingrese el largo de la primera diagonal:"))
        b=float(input("Ingrese el largo de la segunda diagonal:"))
        area=area_rombo(a,b)
    elif figura==4:
        a=float(input("Ingrese el radio del circulo:"))
        area=area_circulo(a)
    print("El area de la figura es", area)