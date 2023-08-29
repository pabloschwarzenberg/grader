from math import pi

def area_triangulo(base=None, altura=None):
    return (base * altura) / 2

def area_rectangulo(base=None, altura=None):
    return (base * altura)

def area_rombo(mayor=None, menor=None):
    return (mayor*menor)/2

def area_circulo(radio=None):
    return pi * radio**2
def decision ():
    while True:
        print("Calculadora geométrica")
        print("Área de un triángulo --> 1")
        print("Área de un rectángulo --> 2")
        print("Área de un rombo --> 3")
        print("Área de un círculo --> 4")
        print("Si desea salir --> 5")
        name = int(input("Ingrese la operación que desea calcular: "))
        if name == 5:
            break
        if name == 1:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            x = area_triangulo(b, a)
            print(x)

        if name == 2:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            x = area_rectangulo(b, a)
            print(x)

        if name == 3:
            m = float(input("ingrese la diagonal mayor: "))
            me = float(input("Ingrese la diagonal menor: "))
            x = area_rombo(m, me)
            print(x)

        if name == 4:
            r = float(input("Ingrese el radio del circulo: "))
            x = area_circulo(r)
            print(x)