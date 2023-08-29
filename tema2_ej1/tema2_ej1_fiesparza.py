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
    import math
    pi=3.141592653589793
    area=pi*radio**2 
    
radio=int(input(("ingrese radio"))

base=int(input("ingrese base"))
altura=int(input("ingrese altura"))
diagonal1=int(input("ingrse diagonal1"))
diagonal2=int(input("ingrse daiagonal2"))
a=area_circulo()
b=area_triangulo()
c=area_rectangulo()
d=area_rombo()

escoga=input("ingrese eleccion")

