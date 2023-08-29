def area_triangulo(base,altura):
    area = (base * altura)/2
    return area
    

def area_rectangulo(base,altura):
    area = base * altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
from math import pi 
def area_circulo(radio):
    area = pi * radio **2
    return area

if __name__ == "__main__":
    radio = int(input("ingresa radio: "))
    base = float(input("ingresa largo: "))
    altura= float(input("ingresa ancho: "))
    lado = float(input("Ingrese lado: "))
    base = float(input("ingrese base: "))
    altura = float(input("ingrese altura: "))
    diagonal1 = float(input("ingrese diagonal1: "))
    diagonal2 = float(input("ingrese diagonal2: "))    
    
           