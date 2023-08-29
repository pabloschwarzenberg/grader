import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)

if __name__ == "__main__":
    print("Seleccione la figura geométrica:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingrese su opción (1-4): "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print(area)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print(area)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        area = area_rombo(diagonal_mayor, diagonal_menor)
        print(area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print(area)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")