from math import pi

def area_triangulo(base,altura):
    areat= (base*altura)/2
    return areat
    pass

def area_rectangulo(base,altura):
    arear = base * altura
    return arear
    pass

def area_rombo(diagonal1,diagonal2):
    arearombo = ((diagonal1*diagonal2)/2)
    return arearombo
    pass

def area_circulo(radio):
    areac = (pi*(radio**2))
    return areac
    pass

if __name__ =="__main__":
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
           