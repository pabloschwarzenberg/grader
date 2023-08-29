# Construye un programa que permita calcular el área de :
# un rectángulo
# un triángulo
# un rombo 
# un círculo
# creando una función específica para cada figura geométrica y con un menú que permita elegir lo que la persona desea calcular. 
# (Importa desde la librería math, la constante pi).
import math

def area_triangulo(base,altura):
    a_triangulo=((base*altura)/2)
    return a_triangulo

def area_rectangulo(base,altura):
    a_rectangulo=base*altura
    return a_rectangulo

def area_rombo(diagonal1,diagonal2):
    a_rombo=((diagonal1*diagonal2)/2)
    return a_rombo

def area_circulo(radio):
    a_circulo=(math.pi*(radio**2))
    return a_circulo

if __name__ == "__main__":
    base=float(input("escriba la base de su figura: "))
    altura=float(input("escriba la altura de su figura: "))
    diagonal1=float(input("escriba la diagonal1 de su figura: "))
    diagonal2=float(input("escriba la diagonal2 de su figura: "))
    radio=float(input("escriba el radio de su figura"))

    print("el area del triangulo es ",area_triangulo(base,altura))
    print("el area del rectangulo es ",area_rectangulo(base,altura))
    print("el area del rombo es ",area_rombo(diagonal1,diagonal2))
    print("el area del circulo es ",area_circulo(radio))