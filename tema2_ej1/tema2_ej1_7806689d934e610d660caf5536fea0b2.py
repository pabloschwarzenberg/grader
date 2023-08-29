import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return(area)
def area_rombo(D1,D2):
    area=(D1*D2)/2
    return(area)
def area_rectangulo(base,altura):
    area=base*altura
    return(area)
def area_circulo(radio):
    area=math.pi*(radio)**2
    return(area)
if __name__=="__main__":
    a=input("ingrese el nombre de la figura a la que quiere calcular el área: ")
    if a=="triangulo":
        base=input("ingrese base: ")
        altura=input("ingrese altura: ")
        print(area_triangulo(base,altura))
    if a=="rectangulo":
        base=input("ingrese base: ")
        altura=input("ingrese altura: ")
        print(area_rectangulo(base,altura))
    if a=="rombo":
        D1=input("ingrese diagonal1: ")
        D2=input("ingrese diagonal2: ")
        print(area_rombo(D1,D2))
    if a=="circulo":
        radio=input("ingrese radio: ")
        print(area_circulo(radio))
        
        
     
     
    

           