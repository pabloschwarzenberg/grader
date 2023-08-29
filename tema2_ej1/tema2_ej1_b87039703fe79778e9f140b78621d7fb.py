import math
def area_triangulo(base,altura):
    a=(base*altura)/2
    return a

def area_rectangulo(base,altura):
    a=base*altura
    return a

def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return a

def area_circulo(radio):
    a=math.pi*(radio**2)
    return a

if __name__ == "__main__":
    print("1=triangulo, 2= rectangulo, 3=rombo y 4=circulo")
    figura=int(input("ingrese el numero de la figura que desea calcular:"))
    if figura==1:
        area_triangulo(base,altura)
        base=int(input("ingrese la base del triangulo:"))
        altura=int(input("ingrese la altura del triangulo:"))
    if figura==2:
        area_rectangulo(base,altura)
        base=int(input("ingrese la base del rectangulo:"))
        altura=int(input("ingrese la altura del rectangulo:"))
    if figura==3:
        area_rombo(diagonal1,diagonal2)
        diagonal1=int(input("ingrese la diagonal 1 del rombo:"))
        diagonal2=int(input("ingrese la diagonal 2 del rombo:"))
    if figura==4:
        area_circulo(radio)
        radio=int(input("ingrese el radio del circulo:"))
    


           