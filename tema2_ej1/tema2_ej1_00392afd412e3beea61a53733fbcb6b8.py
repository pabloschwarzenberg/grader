import math


def area_triangulo(base, altura):
    a = base*altura
    k = a/2
    print(k)

    return k


def area_rectangulo(base, altura):
    k = base*altura

    return k


def area_rombo(diagonal1, diagonal2):
    v = diagonal1*diagonal2
    v2 = v // 2

    return v2


def area_circulo(radio):

    a = math.pi
    b = radio*radio
    k = a*b
    print(k)

    return k


if __name__ == "__main__":
    print("Elija a que figura geometrica busca obtener el área:")
    print(" 1) Triángulo \n 2) Rectángulo \n 3) rombo \n 4) círculo")
    opcion_menu = int(input("..."))
    if opcion_menu == 1:
        n1 = int(input("Ingrese la base: "))
        n2 = int(input("Ingrese la altura: "))
        area_triangulo(n1, n2)

    elif opcion_menu == 2:
        n1 = int(input("Ingrese la base: "))
        n2 = int(input("Ingrese la altura: "))
        area_rectangulo(n1, n2)

    elif opcion_menu == 3:
        n1 = int(input("Ingrese la primera diagonal: "))
        n2 = int(input("Ingrese la segunda diagonal: "))
        area_rombo(n1, n2)

    elif opcion_menu == 4:
        n3 = int(input("Ingrese el radio del círculo: "))
        area_circulo(n3)
