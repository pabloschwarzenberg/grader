import math


def area_triangulo(base,altura):
    return base * altura/2
pass


def area_rectangulo(base,altura):
    return base * altura 
pass


def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 /2 
pass


def area_circulo(radio):
    return math.pi*(radio*radio)
pass


if __name__ == "__main__":
    print("¿que area deseas calcular?: ")
    print("1. area triangulo")
    print("2. area rectangulo")
    print("3. area rombo")
    print("4. area circulo")

    eleccion = input("eleccion: ") 

    if eleccion == '1' or eleccion == 'triangulo':
        a = float(input("base: "))
        b = float(input("altura: "))
        result = area_triangulo(a,b)
        print("El area del triangulo es", result)

    elif eleccion == '2' or eleccion == 'rectangulo':
        a = float(input("base: "))
        b = float(input("altura "))
        result = area_reactangulo(a,b)
        print("El area del rectangulo es", result)

    elif eleccion == '3' or eleccion == 'rombo':
        a = float(input("Diagonal 1: "))
        b = float(input("Diagonal 2: "))
        result = area_rombo(a,b)
        print("El area del rombo es: ", result)

    elif eleccion == '4' or eleccion == 'circulo':
         a = float(input("radio: "))
         result = area_circulo(a)
         print("El area del circulo es: ", result)
pass
