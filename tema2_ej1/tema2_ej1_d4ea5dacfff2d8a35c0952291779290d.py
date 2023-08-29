import math
def area_triangulo(base,altura):
    areat=(base*altura)/2
    return areat
def area_rombo(diagonal1,diagonal2):
    arear=(diagonal1*diagonal2)/2
    return arear
def area_rectangulo(ancho,largo):
    areare=ancho*largo
    return areare
def area_circulo(radio):
    areac=math.pi*(radio**2)
    return areac

if __name__ == "__main__":
 figura=float(input("Introduzca el numero correspondiente a la figura que quiere calcular: Triangulo(1), Rombo(2),Rectangulo(3) o Circulo(4):"))
 if figura==1:
    b=eval(input("Introduzca el valor de su base:"))
    h=eval(input("Introduzca el valor de su altura:"))
    print(area_triangulo(b,h))
 elif figura==2:
    D1=eval(input("Introduzca el valor de su primera diagonal:"))
    D2=eval(input("Introduzca el valor de su segunda diagonal:"))
    print(area_rombo(D1,D2))
 elif figura==3:
    A=eval(input("Introduzca el valor de su ancho:"))
    L=eval(input("Introduzca el valor de su largo:"))
    print(area_rectangulo(A,L))
 elif figura==4:
    R=eval(input("Introduzca el valor de su radio:"))
    print(area_circulo(R))
 else:
    "Mi calculadora no acepta ese valor vuelve"


           