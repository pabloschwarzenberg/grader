import math

def area_triangulo(base,altura):
    return (base*altura)/2
    
def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return radio*radio*math.pi

if __name__ == "__main__":
    figura=str(input("Ingrese figura: "))
    error=True
    while error==True:
        if figura=="triangulo":
            b=float(input("Ingrese base: "))
            h=float(input("Ingrese altura: "))
            print(area_triangulo(b,h))
            error=False
        elif figura=="rectangulo":
            l1=float(input("Ingrese un lado: "))
            l2=float(input("Ingrese otro lado: "))
            print(area_rectangulo(l1,l2))
            error=False
        elif figura=="rombo":
            d1=float(input("Ingrese una diagonal: "))
            d2=float(input("Ingrese otra diagonal: "))
            print(area_rombo(d1,d2))
            error=False
        elif figura=="circulo":
            r=float(input("Ingrese radio: "))
            print(area_circulo(r))
            error=False
        else:
            error=True
            print("ERROR")