import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

def area_triangulo(base, altura):
    return calcular_area_triangulo(base, altura)

def area_rectangulo(base, altura):
    return calcular_area_rectangulo(base, altura)

def area_rombo(diagonal1, diagonal2):
    return calcular_area_rombo(diagonal1, diagonal2)

def area_circulo(radio):
    return calcular_area_circulo(radio)

if __name__ == "__main__":
    print("Bienvenido al programa de cálculo de áreas.")
    print("Por favor, seleccione una opción:")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")

    opcion = int(input("Ingrese el número de la opción seleccionada: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
        area = area_rombo(diagonal_mayor, diagonal_menor)
        print(f"El área del rombo es: {area}")
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print(f"El área del círculo es: {area}")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
       