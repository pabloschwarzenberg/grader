from math import *
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
    
    area=pi*(radio**2)
    return area
if __name__ == "__main__":
    print("esta es uca calculadora geometrica")
    print("calcula area de figuras geomretricas")
    print("presiones 1 para triangulo, 2 para rectangulo, 3 para rombo y 4 para circulo")
    a=int(input(":"))
    if a==1:
        print("ingrese (altura)")
        b=int(input(":"))
        print("ingrese (base)")
        c=int(input(":"))
        area=area_triangulo(c,b)
        print(area)

    elif a==2:
        print("ingrese (base)")
        b=int(input(":"))
        print("ingrese (altura)")
        c=int(input(":"))
        area=area_rectangulo(b,c)
        print(area)

    elif a==3:
        print("ingrese (diagonal1)")
        b=int(input(":"))
        print("ingrese (diagonal2)")
        c=int(input(":"))
        area=area_rombo(b,c)
        print(area)

    elif a==4:
        print("ingrese (radio)")
        b=int(input(":"))
        area=area_circulo(b)
        print(area)

           