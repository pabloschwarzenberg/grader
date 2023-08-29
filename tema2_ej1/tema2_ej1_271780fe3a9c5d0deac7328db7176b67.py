import math

def area_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    return area_triangulo

def area_rectangulo(base, altura):
    area_rectangulo = base * altura
    return area_rectangulo

def area_rombo(diagonal1, diagonal2):
    area_rombo = (diagonal1 * diagonal2) / 2
    return area_rombo

def area_circulo(radio):
    area_circulo = math.pi * radio ** 2
    return area_circulo

def main():
    print("Menu")
    print("1. Area Triangulo")
    print("2. Area Rectangulo")
    print("3. Area del Rombo")
    print("4. Area del Circulo")
    print()

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(area_triangulo(base, altura))

    elif opcion == 2:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        print(area_rectangulo(base, altura))

    elif opcion == 3:
        diagonal1 = int(input("Ingrese la diagonal 1: "))
        diagonal2 = int(input("Ingrese la diagonal 2: "))
        print(area_rombo(diagonal1, diagonal2))

    elif opcion == 4:
        radio = int(input("Ingrese el radio: "))
        print(area_circulo(radio))

if __name__ == "__main__":
    main()

