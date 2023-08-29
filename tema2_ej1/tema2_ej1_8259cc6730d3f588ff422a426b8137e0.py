import math
def area_triangulo(base,altura):
    at=(base*altura)/2
    return at

def area_rectangulo(base,altura):
    ar=base*altura
    return ar

def area_rombo(diagonal1,diagonal2):
    aro=(diagonal1*diagonal2)/2
    return aro

def area_circulo(radio):
    ac=math.pi*((radio)**2)
    return ac

if __name__ == "__main__":
    print("Área de un Triángulo: 0")
    print("Área de un Rectángulo: 1")
    print("Área de un Rombo: 2")
    print("Área de un Círculo: 3")
    n=int(input("Ingrese que desea calcular:"))
    if n==0:
        base=int(input("Base:"))
        altura=int(input("Altura:"))
        print(area_triangulo(base, altura))
    elif n==1:
        base=int(input("Base:"))
        altura=int(input("Altura:"))
        print(area_rectangulo(base,altura))
    elif n==2:
        diagonal1=int(input("Diagonal 1:"))
        diagonal2=int(input("Diagona 2:"))
        print(area_rombo(diagonal1, diagonal2))
    elif n==3:
        radio=int(input("Radio:"))
        print(area_circulo(radio))

           