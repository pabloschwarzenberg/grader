import math

def area_triangulo(base,altura):
    area=(base*altura)/2
    pass
    return area

def area_rectangulo(lado1,lado2):
    area=lado1*lado2
    pass
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    pass
    return area
    
def area_circulo(radio):
    area=math.pi*radio**2
    pass
    return area

def menu():
    print("-------Calculadora de areas---------")
    print("1.Area triangulo")
    print("2.Area rectangulo")
    print("3.Area rombo")
    print("4.Area circulo")
    print("5.Salir")

    opcion=int(input("Ingrese una opcion:"))
    if opcion==1:
        base=int(input("Ingrese la base:"))
        altura=int(input("Ingrese la altura:"))
        triangulo=area_triangulo(base,altura)
        print(triangulo)

    if opcion==2:
        lado1=int(input("Ingrese el lado 1:"))
        lado2=int(input("Ingrese el lado 2:"))
        rectangulo=area_rectangulo(lado1,lado2)
        print(rectangulo)

    if opcion==3:
        diagonal1=int(input("Ingrese la diagonal 1:"))
        diagonal2=int(input("Ingrese la diagonal 2:"))
        rombo=area_rombo(diagonal1,diagonal2)
        print(rombo)

    if opcion==4:
        radio=int(input("Ingrese el radio:"))
        circulo=area_circulo(radio)
        print(circulo)

    if opcion==5:
        sys.exit()
           