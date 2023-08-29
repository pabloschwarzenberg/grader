import math
def area_triangulo(base,altura):
    area=base*altura/2
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
if __name__ == "__main__":
    print("que area quieres saber")
    print("1.triangulo")
    print("2.rectangulo")
    print("3.rombo")
    print("4.circulo")
    a=int(input())
    if a==1:
        base=int(input("base: "))
        altura=int(input("altura: "))
        area_triangulo(base,altura)
        print(area_triangulo(base,altura))
    elif a==2:
        base=int(input("base: "))
        altura=int(input("altura: "))
        area_rectangulo(base,altura)
        print(area_rectangulo(base,altura))
    elif a==3:
        diagonal1=int(input("diagonal 1: "))
        diagonal2=int(input("diagonal 2: "))
        area_rombo(diagonal1,diagonal2)
        print(area_rombo(diagonal1,diagonal2))
    elif a==4:
        radio=int(input("radio: "))
        area_circulo(radio)
        print(area_circulo(radio))