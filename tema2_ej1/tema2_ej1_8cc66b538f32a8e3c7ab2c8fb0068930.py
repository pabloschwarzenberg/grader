import math
math.pi

def area_triangulo(base,altura):
    a=(altura*base)/2
    return a

def area_rectangulo(base,altura):
    a=base*altura
    return a

def area_rombo(diagonal1,diagonal2):
    a=(diagonal1*diagonal2)/2
    return a

def area_circulo(radio):
    a=(math.pi)*radio*radio
    return a


if __name__ == "__main__":
    accion=int(input("""1=Triángulo
    2=Rectángulo
    3=Rombo
    4=Círculo
    Ingrese acción: """))


    if accion==1:
        base=int(input("Base: "))
        altura=int(input("Altura: "))
        area_triangulo(base,altura)
        print(area_triangulo(base,altura))

    elif accion==2:
        base=int(input("Base: "))
        altura=int(input("Altura: "))
        area_rectangulo(base,altura)
        print(area_rectangulo(base,altura))

    elif accion==3:
        diagonal1=int(input("Diagonal 1: "))
        diagonal2=int(input("Diagonal 2: "))
        area_rombo(diagonal1,diagonal2)
        print(area_rombo(diagonal1,diagonal2))

    elif accion==4:
        radio=int(input("Radio: "))
        area_circulo(radio)
        print(area_circulo(radio))
           