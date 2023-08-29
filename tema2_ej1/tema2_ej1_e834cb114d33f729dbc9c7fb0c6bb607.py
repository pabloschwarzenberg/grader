import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1 * diagonal2)/2
    return area

def area_circulo(radio):
    area = math.pi*radio**2
    return area

if __name__ == "__main__":
    print("1) Triangulo")
    print("2) rectangulo")
    print("3) rombo")
    print("4) circulo")
    name= int(input("¿De qué figura desea culcular el area?:"))
    if name==1:
        base=int(input("ingrese base del triangulo:"))
        altura= int(input ("ingrese altura del triangulo:"))
        print("el area del triangulo es:", area_triangulo(base , altura))
    elif name==2:
        base=int(input("ingrese base del rectangulo:"))
        altura= int(input ("ingrese altura del rectangulo:"))
        print("el area del rectangulo es:", area_rectangulo(base , altura))
    elif name==3:
        diagonal1= int(input("ingrese la diagonal 1 del rombo:"))
        diagonal2= int(input("ingrese la diagonal 2 del rombo:"))
        print("el area del rombo es:",area_rombo(diaigonal1,diagonal2))
    elif name==4:
        radio=int(input("ingrese radio del circulo:"))
        print("el area del circulo es:",area_circulo(radio))
    else:
        print(" no puedo calcular eso")

