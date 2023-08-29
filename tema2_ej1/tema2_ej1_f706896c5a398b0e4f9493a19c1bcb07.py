import math

def area_triangulo(base,altura):
    a=(base*altura)/2
    return a
    pass

def area_rectangulo(base,altura):
    a=(base*altura)
    return a
    pass

def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return a
    pass

def area_circulo(radio):
    a=(radio**2)*math.pi
    return a
    pass

if __name__ == "__main__":
    pass
    print("Este programa puede calcular el area de un: ")
    print("Triangulo")
    print("Rectangulo")
    print("Rombo")
    print("Circulo")
    opcion=input("Que area quieres calcular: ")
    if opcion=="Triangulo":
        b=int(input("Ingrese base: "))
        a=int(input("Ingrese altura: "))
        unidad=input("Ingrese unidades: ")
        print("El area de tu triangulo es: " + str(area_triangulo(b,a)) + unidad + "^2")
    if opcion=="Rectangulo":
        b=int(input("Ingrese base: "))
        a=int(input("Ingrese altura: "))
        unidad=input("Ingrese unidades: ")
        print("El area de tu rectangulo es: " + str(area_rectangulo(b,a)) + unidad + "^2")
    if opcion=="Rombo":
        d1=int(input("Ingrese diagonal1: "))
        d2=int(input("Ingrese diagonal2: "))
        unidad=input("Ingrese unidades: ")
        print("El area de tu rombo es: " + str(area_rombo(d1,d2)) + unidad + "^2")
    if opcion=="Circulo":
        r=int(input("Ingrese radio: "))
        unidad=input("Ingrese unidades: ")
        print("El area de tu circulo es: " + str(area_circulo(r)) + unidad + "^2")