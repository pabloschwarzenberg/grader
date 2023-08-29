import math
Pi = math.pi
Redondeo = round(Pi, 2)

def area_triangulo(base,altura):
    area_tri = (base * altura)/2
    return area_tri

def area_rectangulo(base,altura):
    area_re = base * altura
    return area_re

def area_rombo(diagonal1,diagonal2):
    area_ro = (diagonal1 * diagonal2)/2
    return area_ro

def area_circulo(Radio):
    area_cir = Pi * Radio**2 
    return area_cir
    
if __name__ == "__main__":
    
    Base_tri = int(input("Ingrese la base del triangulo:"))
    Altura_tri = int(input("Ingrese la altura del triángulo:"))
    print("El area de su triángulo es:",area_triangulo(Base_tri, Altura_tri))
    
    Base_rec = int(input("Ingrese la base del rectangulo:"))
    Altura_rec = int(input("Ingrese la altura del rectangulo:"))
    print("El area de su rectángulo es:",area_Rectangulo(Base_rec, Altura_rec))
    
    Dia_Rom_1 = int(input("Ingrese la primera diagonal del rombo:"))
    Dia_Rom_2 = int(input("Ingrese la segunda diagonal del rombo:"))
    print("El area de su rombo es:", area_Rombo(Dia_Rom_1, Dia_Rom_2))
    
    Radio_Cir = int(input("Ingrese el radio del circulo:"))
    print("El area de su círculo es:",area_Circulo(Radio_Cir))