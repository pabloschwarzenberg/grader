import math
def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(Diagonal,Diagonal2):

    area=(Diagonal * Diagonal2)/2
    return area
def area_circulo(radio):
    area=math.pi*radio**2
    return area
if __name__ == "__main__":
    print("Que area quires calcular")
    print("1.Triangulo, 2.Rectangulo, 3.Rombo, 4.Circulo")
    x= int(input())
    if x == 1:
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        area_triangulo(base, altura)
        print(area_triangulo(base,altura))
    elif x == 2:
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        area_rectangulo(base, altura)
        print(area_rectangulo(base, altura))
    elif x== 3:
        Diagonal =int(input("Diagonal: "))
        Diagonal2 =int(input("Diagonal 2 : "))
        area_rombo(Diagonal,Diagonal2)
        print(area_rombo(Diagonal, Diagonal2))
    elif x == 4:
        radio=int(input("Radio: "))
        area_circulo(radio)
        print(area_circulo(radio))

