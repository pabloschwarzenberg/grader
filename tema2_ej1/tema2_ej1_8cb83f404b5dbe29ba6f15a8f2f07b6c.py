import math

def area_rectangulo(base, altura):
    return (base)*(altura)
def area_triangulo(base,altura):
    return (base)*(altura)/2
def area_rombo(D,d):
    return (D)*(d)/2
def area_circulo(r):
    return math.pi*r**2

if __name__ == "__main__":
    print("Utilze 1=rectángulo, 2=triángulo, 3=rombo y 4=círculo ")
    figura=int(input("Ingrese la figura con la que desea trabajar: "))
    if figura == (1):
        base=int(input("Ingrese base del rectángulo: "))
        altura=int(input("Ingrese altura del rectángulo: "))  
        print("El área del rectángulo es: ", area_rectangulo(base, altura))
    elif figura == (2):
        base=int(input("Ingrese base del triángulo: "))
        altura=int(input("Ingrese altura del triángulo: "))
        print("El área del rectángulo es: ", area_triangulo(base, altura))
    elif figura == (3):
        D=int(input("Ingrese diagonal mayor del rombo: "))
        d=int(input("Ingrese diagonal menor del rombo: "))
        print("El área del rectángulo es: ", area_rombo(D, d))
    elif figura == (4):
        r=int(input("Ingrese radio del círculo: "))
        print("El área del rectángulo es: ", area_circulo(r))