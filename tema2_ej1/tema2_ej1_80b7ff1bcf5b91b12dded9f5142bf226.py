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
    area=(math.pi)*(radio**2)
    return area

if __name__ == "__main__":
    print("1:area triangulo")
    print("2:area reactangulo")
    print("3:area rombo")
    print("4:area circulo")
    x=int(input("Eliga el area que desea calcular"))
    if x==1:
        b=int(input("base: "))
        a=int(input("altura: "))
        print(area_triangulo(b,a))
    elif x==2:
        b=int(input("base: "))
        a=int(input("area: "))
        print(area_rectangulo(b,a))
    elif x==3:
        d1=int(input("primera diagonal: "))
        d2=int(input("segunda diagonal: "))
        print(area_rombo(d1,d2))
    elif x==4:
        r=int(input("radio: "))
        print(area_circulo(r))
           