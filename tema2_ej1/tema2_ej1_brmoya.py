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
    area=radio*radio*math.pi
    return area

if __name__=="__main__":
    print("(0)Area triangulo")
    print("(1)Area rectangulo")
    print("(2)Area rombo")
    print("(3)Area circulo")
    area=int(input("Que area desea calcular?: "))
    if area==0:
        base=int(input("ingrese la base: "))
        altura=int(input("ingrese su altura: "))
        print (area_triangulo(base,altura))
    elif area==1:
        base = int(input("ingrese la base: "))
        altura = int(input("ingrese su altura: "))
        print(area_rectangulo(base, altura))
    elif area==2:
        diagonal1=int(input("ingrese la diagonal 1: "))
        diagonal2=int(input("ingrese la diagonal 2: "))
        print(area_rombo(diagonal1,diagonal2))
    elif area==3:
        radio=int(input("ingrese el radio: "))
        print(area_circulo(radio))