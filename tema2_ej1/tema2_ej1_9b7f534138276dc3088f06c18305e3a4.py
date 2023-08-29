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

def menu_figuras():
    a=input("Ingrese el área que desea calcular (triangulo,rectangulo,rombo o circulo: ")
    a=a.lower()
    if a=="triangulo":
        b=int(input("Ingrese base: "))
        h=int(input("Ingrese altura: "))
        return area_triangulo(b,h)
    elif a=="rectangulo":
        b=int(input("Ingrese base: "))
        h=int(input("Ingrese altura: "))
        return area_rectangulo(b,h)
    elif a=="rombo":
        b=int(input("Ingrese una diagonal: "))
        h=int(input("Ingrese la otra diagonal: "))
        return area_rombo(b,h)
    elif a=="circulo":
        r=int(input("Ingrese radio: "))
        return area_circulo(r)

if __name__ == "__main__":
    pass
           