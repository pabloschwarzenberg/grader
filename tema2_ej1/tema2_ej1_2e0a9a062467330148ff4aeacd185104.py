from math import pi

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return pi * radio**2

if __name__ == "__main__":
    while True:
        print("Menú:")
        print("1. Calcular el área de un rectángulo")
        print("2. Calcular el área de un triángulo")
        print("3. Calcular el área de un rombo")
        print("4. Calcular el área de un círculo")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            print("El área del rectángulo es: {}".format(area_rectangulo(base, altura)))
        elif opcion == 2:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            print("El área del triángulo es: {}".format(area_triangulo(base, altura)))
        elif opcion == 3:
            diagonal_mayor = float(input("Introduce la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Introduce la diagonal menor del rombo: "))
            print("El área del rombo es: {}".format(area_rombo(diagonal_mayor, diagonal_menor)))
        elif opcion == 4:
            radio = float(input("Introduce el radio del círculo: "))
            print("El área del círculo es: {}".format(area_circulo(radio)))
        elif opcion == 5:
            break
