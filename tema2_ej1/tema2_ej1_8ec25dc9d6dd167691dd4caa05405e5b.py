import math

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_rombo(diagonal1, diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    print("Bienvenido al programa de cálculo de áreas")
    print("1. Calcular área del triángulo")
    print("2. Calcular área del rectángulo")
    print("3. Calcular área del rombo")
    print("4. Calcular área del círculo")

    opcion = int(input("Ingrese el número correspondiente a la figura: "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)

    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)

    elif opcion == 3:
        diagonal1 = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal2 = float(input("Ingrese la diagonal menor del rombo: "))
        area = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", area)

    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
