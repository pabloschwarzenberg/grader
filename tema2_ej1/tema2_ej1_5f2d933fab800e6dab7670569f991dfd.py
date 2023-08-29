import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    while True:
        print("1. Calcular área del triángulo")
        print("2. Calcular área del rectángulo")
        print("3. Calcular área del rombo")
        print("4. Calcular área del círculo")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == 2:
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            area = area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == 3:
            diagonal1 = float(input("Ingresa la primera diagonal del rombo: "))
            diagonal2 = float(input("Ingresa la segunda diagonal del rombo: "))
            area = area_rombo(diagonal1, diagonal2)
            print("El área del rombo es:", area)
        elif opcion == 4:
            radio = float(input("Ingresa el radio del círculo: "))
            area = area_circulo(radio)
            print("El área del círculo es:", area)
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")
