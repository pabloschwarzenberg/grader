import math

def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area
def area_circulo(radio):
    area=radio**2*math.pi
    return area
    
if __name__ == "__main__":
    figura=str(input("Ingrese figura:"))
    if figura=="triangulo":
        base=float(input("Ingrese base: "))
        altura=float(input("Ingrese altura: "))
        print("El area es: ",area_triangulo(base,altura))
    elif figura=="rectangulo":
        base=float(input("Ingrese base: "))
        altura=float(input("Ingrese altura: "))
        print("El area es: ",area_rectangulo(base,altura))
    elif figura=="rombo":
        diagonal1=float(input("Ingrese diagonal1: "))
        diagonal2=float(input("Ingrese diagonal2: "))
        print("El area es: ",area_rombo(diagonal1,diagonal2))
    elif figura=="circulo":
        radio=float(input("Ingrese radio: "))
        print("El es: ",area_circulo(radio))