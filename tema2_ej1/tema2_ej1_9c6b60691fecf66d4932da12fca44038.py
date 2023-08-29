import math
def area_triangulo(base,altura):
    return base*altura/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

def area_circulo(radio):
    return math.pi*radio*radio

if __name__ == "__main__":
    print("1) Area triangulo/n2) Area rectangulo/n3) Area rombo/n4) Area circulo")
    n=input("¿Qué desea calcular?")
    if n=="1":
        base=int(input("Ingrese base: "))
        altura=int(input("ingrese altura: "))
        print(area_triangulo(base,altura))
    elif n=="2":
        base=int(input("Ingrese base: "))
        altura=int(input("ingrese altura: "))
        print(area_rectangulo(base,altura))
    elif n=="3":
        diagonal1=int(input("ingrese diagonal 1: "))
        diagonal2=int(input("ingrese diagonal 2: "))
        print(area_rombo(diagonal1,diagonal2))
    elif n=="4":
        radio=int(input("ingrese radio: "))
        print(area_circulo(radio))
    
