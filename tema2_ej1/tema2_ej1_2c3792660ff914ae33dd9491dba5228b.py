import math


def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area=(math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    pass
    a=input("Si desea el area de un triangulo, ingrese t, si desea el area de un rectangulo, ingrese r, si desea el area de un rombo, ingrese ro, si desea el area de un círculo, ingrese c: ")
    if a=="t":
        base1=int(input("Ingrese la base del triangulo: "))
        altura1=int(input("Ingrese la altura del triangulo: "))
        print(area_triangulo(base1,altura1))
    elif a=="r":
        base2=int(input("Ingrese la base del rectangulo: "))
        altura2=int(input("Ingrese la altura del rectangulo: "))
        print(area_rectangulo(base2,altura2))
    elif a=="ro":
        d1=int(input("Ingrese la diagonal1 del rectangulo: "))
        d2=int(input("Ingrese la diagonal2 del rectangulo: "))
        print(area_rombo(d1,d2))
    elif a=="c":
        radio=int(input("Ingrese el radio del círculo: "))
        print(area_circulo(radio))
