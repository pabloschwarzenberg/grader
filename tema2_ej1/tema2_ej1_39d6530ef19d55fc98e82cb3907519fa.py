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
    area=math.pi*radio*radio
    return area

if __name__ == "__main__":
    figura=str(input("¿El area de que figura desea calcular?:"))
    if figura=="rectangulo":
        b=float(input("Ingrese base:"))
        a=float(input("Ingrese altura:"))
        area=area_rectangulo(b,a)
        print(area_rectangulo(b,a))
    elif figura=="rombo":
        k=float(input("ingrese primera diagonal"))
        z=float(input("ingrese segunda diagonal"))
        arear=area_rombo(k,z)
        print (area_rombo(k,z))
    elif figura=="triangulo":
        b=float(input("ingrese base del triangulo:"))
        h=float(input("ingrese altura del triangulo:"))
        areaf=area_triangulo(b,h)
        print(area_triangulo(b,h))
    elif figura=="circulo":
        r=float(input("ingrese radio del circulo:"))
        areac=area_circulo(r)
        print(area_circulo(r))