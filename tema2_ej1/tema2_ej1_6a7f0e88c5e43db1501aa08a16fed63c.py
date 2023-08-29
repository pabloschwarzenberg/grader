from math import pi

def area_triangulo(base,altura):
    areatri= (base*altura)/2
    return areatri
    pass

def area_rectangulo(base,altura):
    arearec = base * altura
    return arearec
    pass

def area_rombo(diagonal1,diagonal2):
    arearom = ((diagonal1*diagonal2)/2)
    return arearom
    pass

def area_circulo(radio):
    areacir = (pi*(radio**2))
    return areacir
    pass

if print("_main_") == "_main_":
    elegir = input("que area desea calcular?: ")
    if elegir == "triangulo":
        base = int(input("ingrese valor de base: "))
        altura = int(input("ingrese valor de altura: "))
        print(area_triangulo(base,altura))
    if elegir == "rectangulo":
        base = int(input("ingrese valor de base: "))
        altura = int(input("ingrese valor de altura: "))
        print(area_rectangulo(base,altura))
    if elegir == "rombo":
        diagonal1 = int(input("ingrese valor de diagonal 1: "))
        diagonal2 = int(input("ingrese valor de diagonal 2: "))
        print(area_rombo(diagonal1,diagonal2))
    if elegir == "circulo":
        radio = int(input("ingrese valor de radio: "))
        print(area_circulo(radio))
    pass
           