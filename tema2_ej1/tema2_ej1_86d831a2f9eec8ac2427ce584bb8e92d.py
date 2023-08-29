import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    while True:
        print("1. Calcular el area de un rectangulo")
        print("2. Calcular el area de un triangulo")
        print("3. Calcular el area de un rombo")
        print("4. Calcular el area de un circulo")
        print("5. Salir")
        opcion = int(input("Selecciona una opcion: "))

        if opcion == 1:
            base = float(input("Ingresa la base del rectangulo: "))
            altura = float(input("Ingresa la altura del rectangulo: "))
            area = area_rectangulo(base, altura)
            print("El area del rectangulo es", area)
        elif opcion == 2:
            base = float(input("Ingresa la base del triangulo: "))
            altura = float(input("Ingresa la altura del triangulo: "))
            area = area_triangulo(base, altura)
            print("El area del triangulo es", area)
        elif opcion == 3:
            diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
            area = area_rombo(diagonal_mayor, diagonal_menor)
            print("El area del rombo es", area)
        elif opcion == 4:
            radio = float(input("Ingresa el radio del circulo: "))
            area = area_circulo(radio)
            print("El area del circulo es", area)
        elif opcion == 5:
            break