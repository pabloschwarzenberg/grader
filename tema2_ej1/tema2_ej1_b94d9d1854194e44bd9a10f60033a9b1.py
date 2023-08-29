import math

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dados su base y altura.
    """
    return base * altura

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dados su base y altura.
    """
    return base * altura / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo dados sus diagonales mayor y menor.
    """
    return diagonal_mayor * diagonal_menor / 2

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    """
    return math.pi * radio ** 2

if __name__ == "__main__":
    while True:
        print("Seleccione una figura geométrica para calcular su área:")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Rombo")
        print("4. Círculo")
        opcion = int(input("Ingrese el número de la opción deseada (1-4): "))

        if opcion == 1:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print("El área del rectángulo es:", area_rectangulo(base, altura))
        elif opcion == 2:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print("El área del triángulo es:", area_triangulo(base, altura))
        elif opcion == 3:
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            print("El área del rombo es:", area_rombo(diagonal_mayor, diagonal_menor))
        elif opcion == 4:
            radio = float(input("Ingrese el radio del círculo: "))
            print("El área del círculo es:", area_circulo(radio))
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-4).")

        continuar = input("¿Desea continuar? (S/N)").upper()
        if continuar != "S":
            break
