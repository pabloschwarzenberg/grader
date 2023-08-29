import math
def area_triangulo(base,altura):
    area = float(base)*float(altura)/2
    return area
    pass

def area_rectangulo(base,altura):
    area = float(base)*float(altura)
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = float(diagonal1)*float(diagonal2)/2
    return area
    pass

def area_circulo(radio):
    area = math.pi*float(radio)**2
    return area
    pass

if __name__ == "__main__":
    eleccion = str(iput("¿que area desea calcular? (triangulo/rectangulo/rombo/circulo): "))
    if eleccion == "triangulo":
        a=float(input("ingrese altura: "))
        b=float(input("ingrese base: "))
        print(area_triangulo(a,b))
    if eleccion == "rectangulo":
        a=float(input("ingrese altura: "))
        b=float(input("ingrese base: "))
        print(area_rectangulo(a,b))
    if eleccion == "rombo":
        a=float(input("ingrese diagonal1: "))
        b=float(input("ingrese diagonal2: "))
        print(area_rombo(a,b))
    if eleccion == "circulo":
        a=float(input("ingrese radio: "))
        print(area_circulo(a))
    pass
           