import math

def area_triangulo(base,altura):
    area = base * altura / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area

def area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    x=int(input("Ingrese funcion para hacer: "))
    if x == 1:
        base=int(input("Ingrese base: "))
        altura=int(input("Ingrese altura: "))
        print(area_triangulo(base,altura))
    else:
        if x == 2:
            base=int(input("Ingrese base: "))
            altura=int(input("Ingrese altura: "))
            print(area_rectangulo(base,altura))
        else:
            if x == 3:
                diagonal1=int(input("Ingrese diagonal1: "))
                diagonal2=int(input("Ingrese diagonal2: "))
                print(area_rombo(diagonal1,diagonal2))
            else:
                if x == 4:
                    radio=int(input("Ingrese radio: "))
                    print(area_circulo(radio))
           