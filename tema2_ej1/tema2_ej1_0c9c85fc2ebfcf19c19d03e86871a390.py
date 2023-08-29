import math
pi =math.pi

def area_triangulo(base,altura):
    area = (base*altura)/2
    return area
    pass

def area_rectangulo(base,altura):
    area = (base * altura)
    return area
    pass

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area
    pass


def area_circulo(radio):
    area = pi*radio**2
    return area
    pass

if __name__ == "__main__":
    print("Calcular area triangulo: Ingrese 1")
    print("Calcular area rectangulo: Ingrese 2")
    print("Calcular area rombo: Ingrese 3")
    print("Calcular area circulo: Ingrese 4")

    seleccion = int(input(""))
    if seleccion==1:
        base= float(input("Ingrese Base: "))
        altura = float(input("Ingrese altura"))
        print(area_triangulo(base,altura))

    elif seleccion==2:
        base = float(input("Ingrese Base: "))
        altura = float(input("Ingrese altura"))
        print(area_rectangulo(base,altura))

    elif seleccion==3:
        diagonal1 = float(input("Ingrese Diagonal1: "))
        diagnonal2 = float(input("Ingrese Diagonal1: "))
        print(area_rectangulo(diagonal1, diagnonal2))

    elif seleccion==4:
        radio = float(input("Ingrese Radio:"))
        print(area_circulo(radio))

    pass