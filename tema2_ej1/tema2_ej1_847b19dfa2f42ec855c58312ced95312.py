def area_triangulo(base,altura):
    area= (base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=(base*altura)
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area 
import math
def area_circulo(radio):
    area = (radio**2)*(math.pi)
    return area
areas= area_circulo, area_rombo, area_rectangulo, area_triangulo

if __name__ == "__main__":
    base = float(input())
    altura= float(input())
    diagonal1 = float(input())       
    diagonal2=float(input())
    radio= float(input())
    eleccion = input()
    
    