import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("Bienvenido al programa de cálculo de áreas.")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Selecciona una opción (1-4): "))

    if opcion == 1:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print("El área del rectángulo es:", area)
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
        area = area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", area)
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        area = area_circulo(radio)
        print("El área del círculo es:", area)
    else:
        print("Opción inválida. Por favor, selecciona una opción válida (1-4).")

           