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
    area=((math.pi)*(radio*radio))
    return area
    
    


print("¿Qué desea calcular?")
print("1) un rectangulo")
print("2) un triangulo")
print("3) un rombo")
print("4) un circulo")
deseo=3

if deseo==1:
    base=int(input("Ingrese su base:"))
    altura=int(input("Ingrese su Altura:"))
    print(area_rectangulo(base,altura))

elif deseo==2:
    base=int(input("Ingrese su base:"))
    altura=int(input("Ingrese su Altura:"))
    print(area_triangulo(base,altura))

elif deseo==3:
    diagonal1=4
    diagonal2=3
    print(area_rombo(diagonal1,diagonal2))

elif deseo==4:
    radio=int(input("Ingrese su radio:"))
    print(area_circulo(radio))