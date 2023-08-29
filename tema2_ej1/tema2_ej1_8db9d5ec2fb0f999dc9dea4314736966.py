import math

def area_rectangulo(base,altura):
    return base*altura

def area_triangulo(base,altura):
    return (base*altura)/2

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    print("""
    INGRESE LA OPCION A ELEGIR!!
    1.Rectanguulo
    2.Triangulo
    3.Rombo
    4.Circulo
    """)
    a = int(input('Ingrese la opción a elegir: '))
    if a == 1:
        base = float(input("Igrese la base:"))
        altura = float(input("Ingrese la altura: "))
        e = area_rectangulo(base,altura)
        print("El area correspondiente es",e)
    elif a == 2:
        base = float(input("Igrese la base:"))
        altura = float(input("Ingrese la altura: "))
        e = area_triangulo(base,altura)
        print("El area correspondiente es",e)
    elif a == 3:
        diagonal1 = float(input("Ingrese el diagonal 1:"))
        diagonal2 = float(input("Ingrese el diagonal 2:"))
        e = area_rombo(diagonal1,diagonal2)
        print("El area correspondiente es",e)
    elif a == 4:
        radio = float(input("Ingrese el radio:"))
        e = area_circulo(radio)
        print("El area correspondiente es",e)
    else:
        print("Opción no valida")