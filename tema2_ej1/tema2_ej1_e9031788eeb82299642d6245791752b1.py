from math import pi

def area_triangulo(b=None, a=None):
    return (b* a) / 2

def area_rectangulo(b=None, a=None):
    return (b * a)

def area_rombo(diamay=None, diamen=None):
    return (diamay*diamen)/2

def area_circulo(radio=None):
    return pi * radio**2
def decision ():
    while True:
        print("Calculadora geométrica")
        print("Área rectángulo = 32")
        print("Área triángulo = 17")
        print("Área circulo = 22")
        print("Área rombo = 18")
        print("Si usted quiere salir = 0")
        name = int(input("Ingrese operación a calcular: "))
        if name == 0:
            break
        if name == 32:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            x = a_rectangulo(b, a)
            print(x)
            
        if name == 17:
            b = float(input("ingrese la base: "))
            a = float(input("Ingrese la altura: "))
            x = a_triangulo(b, a)
            print(x)

            if name == 22:
                radio = float(input("Ingrese el radio del circulo: "))
            x = a_circulo(radio)
            print(x)

        if name == 18:
            diamay = float(input("ingrese la diagonal mayor: "))
            diamen = float(input("Ingrese la diagonal menor: "))
            x = a_rombo(diamay, diamen)
            print(x)