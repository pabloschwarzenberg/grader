from math import pi

def area_triangulo(base=None, altura=None):
    return (base * altura) / 2

def area_rectangulo(base=None, altura=None):
    return (base * altura)

def area_rombo(dmay=None, dmen=None):
    return (dmay*dmen)/2

def area_circulo(radio=None):
    return pi * radio**2
def decision ():
    while True:
        print("Calculadora geométrica")
        print("Área de triángulo --> 1")
        print("Área de rectángulo --> 2")
        print("Área de rombo --> 3")
        print("Área de círculo --> 4")
        print("Si desea salir --> 5")
        x = int(input("Ingrese la operación que desea calcular: "))
        if x == 5:
            break
        if x == 1:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            y = area_triangulo(b, a)
            print(y)

        if x == 2:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            y = area_rectangulo(b, a)
            print(y)

        if x == 3:
            d1 = float(input("ingrese la diagonal mayor: "))
            d2 = float(input("Ingrese la diagonal menor: "))
            y = area_rombo(d1, d2)
            print(y)

        if x == 4:
            r = float(input("Ingrese el radio del circulo: "))
            y = area_circulo(r)
            print(y)