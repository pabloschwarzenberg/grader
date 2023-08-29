import math
# Construye un programa que permita calcular el área de un rectángulo, un triángulo, un rombo y un círculo, creando una
# función específica para cada figura geométrica y con un menú que permita escoger lo que la persona desea calcular.

def area_triangulo(base,altura):

    base=float(base)
    altura=float(altura)
    AreaT = (base * altura)/2

    return AreaT

def area_rectangulo(base,altura):

    base=float(base)
    altura=float(altura)
    AreaRect = base * altura

    return AreaRect

def area_rombo(diagonal1,diagonal2):

    diagonal1=float(diagonal1)
    diagonal1=float(diagonal1)
    AreaRombo = (diagonal1 * diagonal2)/2

    return AreaRombo

def area_circulo(radio):

    radio=float(radio)
    AreaC = math.pi * (radio ** 2)

    return AreaC

if __name__ == "__main__":
    pass

    Forma = input("Que forma desea: Triangulo, Rectangulo, Rombo o Circulo: ").upper().rstrip()
    
    if Forma == "TRIANGULO":
    
        base = float(input("Ingresar base: "))
        altura = float(input("Ingresar la altura: "))
        print(area_triangulo(base, altura))
    
    
    if Forma == "RECTANGULO":
    
        base = float(input("Ingresar base: "))
        altura = float(input("Ingresar la altura: "))
        print(area_rectangulo(base, altura))
    
    if Forma == "ROMBO":
    
        diagonal1 = float(input("Ingresar primera diagonal: "))
        diagonal2 = float(input("Ingresar segunda diagonal: "))
        print(area_rombo(diagonal1, diagonal2))
    
    
    if Forma == "CIRCULO":
    
        radio = float(input("Ingresar radio de la circunferencia: "))
        print(area_circulo(radio))
           