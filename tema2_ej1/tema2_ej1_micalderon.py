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
    area = math.pi*(radio**2)
    return area

if __name__ == "__main__":
    a = int(input("Que desea calcular:\n1) Area triangulo\n2) Area rectangulo\n3) Area rombo\n4) Area circulo\n"))
    if a == 1:
        b = float(input("Ingrese la base del triangulo:\n"))
        c = float(input("Ingrese la altura del triangulo:\n"))
        print(area_triangulo(b,c))
    if a == 2:
        b = float(input("Ingrese la base del rectangulo:\n"))
        c = float(input("Ingrese la altura del rectangulo:\n"))
        print(area_rectangulo(b,c))
    if a == 3:
        b = float(input("Ingrese la primera diagonal del rombo:\n"))
        c = float(input("Ingrese la segunda diagonal del rombo:\n"))
        print(area_rombo(b,c))
    if a == 4:
        b = float(input("Ingrese el radio del circulo:\n"))
        print(area_circulo(b))