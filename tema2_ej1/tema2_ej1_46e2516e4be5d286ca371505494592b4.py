import math

def area_triangulo(base,altura):
    Area=(base*altura)/2
    return Area

def area_rectangulo(base,altura):
    Area=base*altura
    return Area

def area_rombo(diagonal1,diagonal2):
    Area=(diagonal1*diagonal2)/2
    return Area

def area_circulo(radio):
    Area=math.pi*((radio)**2)
    return Area

if __name__ == "__main__":
    decision=int(input("Que desea calcular?\n1: Triangulo\n2: Rectangulo \n3: Rombo\n4: Circulo\nCalcular: "))
    if decision==1:
        base=float(input("Ingrese la base de su triangulo: "))
        altura=float(input("Ingrese la altura de su triangulo"))
        area_triangulo(base, altura)
    if decision==2:
        base=float(input("Ingrese la base de su rectangulo: "))
        altura=float(input("Ingrese la altura de su rectangulo"))
        area_rectangulo(base, altura)
    if decision==3:
        diagonal1=float(input("Ingrese la base de su rombo: "))
        diagonal2=float(input("Ingrese la altura de su rombo"))
        area_rombo(diagonal1, diagonal2)
    if decision==4:
        radio=float(input("Ingrese el radio de su circulo: "))
        area_circulo(radio)


