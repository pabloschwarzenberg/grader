from math import pi
def area_triangulo(base,altura):
    return (base*altura)/2
def area_rectangulo(base,altura):
    return base*altura
def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2
def area_circulo(radio):
    return pi*radio**2
if __name__ == "_main_":
    a_calcular=int(input("¿Que desea calcular?\n1) areatriangulo \n2) arearectangulo \n3) arearombo \n4) areacirculo")) 
           