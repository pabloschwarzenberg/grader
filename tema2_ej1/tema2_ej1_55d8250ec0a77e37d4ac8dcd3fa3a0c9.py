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
        print("Área de un triángulo --> 1")
        print("Área de un rectángulo --> 2")
        print("Área de un rombo --> 3")
        print("Área de un círculo --> 4")
        print("Si desea salir --> 5")
        name = int(input("Ingrese la operación que desea calcular: "))
        if name == 5:
            break
        if name == 1:
            base = float(input("ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            k = area_triangulo(base, altura)
            print(k)

        if name == 2:
            base = float(input("ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            k = area_rectangulo(base, altura)
            print(k)

        if name == 3:
            dmay = float(input("ingrese la diagonal mayor: "))
            dmen = float(input("Ingrese la diagonal menor: "))
            k = area_rombo(dmay, dmen)
            print(k)

        if name == 4:
            radio = float(input("Ingrese el radio del circulo: "))
            k = area_circulo(radio)
            print(k)

if __name__ == "__main__":
    pass
           