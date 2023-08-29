import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

def mostrar_menu():
    print("1. Calcular área del rectángulo")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del rombo")
    print("4. Calcular área del círculo")

def main():
    opcion = 0
    while opcion != 5:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-5): "))

        if opcion == 1:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == 2:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == 3:
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
            print("El área del rombo es:", area)
        elif opcion == 4:
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area)
        elif opcion == 5:
            print("Hasta luego")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()