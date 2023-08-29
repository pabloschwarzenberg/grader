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
    area=math.pi*radio**2
    return area
if __name__ == "__main__":
    r=input("Que operación desea hacer? (area_triangulo,area_rectangulo,area_rombo,area_circulo): ")
    if r == "area_triangulo":
        a=int(input("Ingrese base: "))
        b=int(input("Ingrese altura: "))
        print(area_triangulo(a,b))
    elif r=="area_rectangulo":
        a=int(input("Ingrese base: "))
        b=int(input("Ingrese altura: "))
        print(area_rectangulo(a,b))
    elif r=="area_rombo":
        a=int(input("Ingrese diagonal 1: "))
        b=int(input("Ingrese diagonal 2: "))
        print(area_rombo(a,b))
    elif r=="area_circulo":
        a=int(input("Ingrese radio: "))
        print(area_circulo(a))
    else:
        print("No se puede realizar operación")
