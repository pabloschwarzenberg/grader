import math

print("¿Qué área desea medir?")
print("(1) Rectángulo. (2) Triángulo. (3) Rombo. (4) Círculo.")

figura=int(input("Ingrese el número correspondiente a su opción: "))

def area_rectangulo(b,h):
    if figura=="1":
       b=input("Ingrese base del rectángulo: ")
       h=input("Ingrese altura del rectángulo: ")
       area_rectangulo=b*h
    return area_rectangulo

def area_triangulo(B,H):
    if figura=="2":
       B=input("Ingrese base del triángulo: ")
       H=input("Ingrese altura del triángulo: ")
       area_triangulo=(B*H)/2
       return area_triangulo

def area_rombo(d1,d2):
    if figura=="3":
       d1=input("Ingrese una diagonal del rombo: ")
       d2=input("Ingrese otra diagonal del rombo: ")
       area_rombo=(d1*d2)/2
       return area_rombo

def area_circulo(R):
    if figura=="4":
       R=input("Ingrese área del círculo: ")
       area_circulo=(math.pi)*R**2
       return area_circulo