import math
#area=float()

def area_triangulo(base,altura):
    area=(base*altura)/2
    print(area)
    return(area)   

def area_rectangulo(base,altura):
    area=(base*altura)
    print(area)
    return(area)

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    print(area)
    return(area)

def area_circulo(radio):
    area=(math.pi)*radio**2
    print(area)
    return(area)

if __name__ == "__main__":
    figura=input("Ingrese figura:")          
    if(figura=="triangulo"):
        baseT=float(input("Ingrese base:"))
        alturaT=float(input("Ingrese altura:"))
        area_triangulo(baseT,alturaT)
        
    if(figura=="rectangulo"):
        baseR=float(input("Ingrese base:"))
        alturaR=float(input("Ingrese altura:"))
        area_rectangulo(baseR,alturaR)
        
    if(figura=="rombo"):
        diagonalR1=float(input("Ingrese diagonal 1:"))
        diagonalR2=float(input("Ingrese diagonal2:"))
        area_rombo(diagonalR1,diagonalR2)

    if(figura=="circulo"):
        radioC=float(input("Ingrese radio:"))
        area_circulo(radioC)