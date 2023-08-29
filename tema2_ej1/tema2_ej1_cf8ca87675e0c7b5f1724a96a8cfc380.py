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
    area = math.pi * (radio ** 2)
    return area

if __name__ == "__main__":
    print("Seleccione la figura geométrica:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingrese el número de la opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 3:
        diagonal1 = float(input("Ingrese la diagonal 1 del rombo: "))
        diagonal2 = float(input("Ingrese la diagonal 2 del rombo: "))
        area = area_rombo(diagonal1, diagonal2)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida")
