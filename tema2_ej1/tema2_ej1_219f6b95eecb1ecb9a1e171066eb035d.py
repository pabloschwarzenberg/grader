from math import pi
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return pi*(radio**2)

if __name__ == "__main__":
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        b = float(input("Ingrese base: "))
        a = float(input("Ingrese altura: "))
        area_triangulo(a,b)
    if opcion == 2:
        b = float(input("Ingrese base: "))
        a = float(input("Ingrese altura: "))
        area_rectangulo(a,b)
    if opcion == 3:
        d1 = float(input("Ingrese diagonal 1: "))
        d2 = float(input("Ingrese diagonal 2: "))
        area_rombo(d1,d2)
    if opcion == 4:
        r = float(input("Ingrese radio: "))
        area_circulo(r)
           