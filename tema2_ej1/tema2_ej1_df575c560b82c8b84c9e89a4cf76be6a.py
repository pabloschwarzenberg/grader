import math
def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area = (math.pi)*(radio**2)
    return area
if __name__ == "__main__":
    f = input("Ingrese opración a realizar:\n1) Área triángulo \n2) Área rectángulo \n3) Área rombo \n4) Área círculo \n")
    if f == "1":
        a = int(input("Ingrese altura triángulo:"))
        b = int(input("Ingrese base triángulo:"))
        print(area_triangulo(b,a))
    elif f == "2":
        a = int(input("Ingrese altura rectángulo:"))
        b = int(input("Ingrese base rectángulo:"))
        print(area_rectangulo(b,a))
    elif f == "3":
        a = int(input("Ingrese diagonal 1 rombo:"))
        b = int(input("Ingrese diagonal 2 rombo:"))
        print(area_rombo(b,a))
    elif f == "4":
        a = int(input("Ingrese radio del círculo:"))
        print(area_circulo(a))
    else:
        print("Operación inválida")
    
           