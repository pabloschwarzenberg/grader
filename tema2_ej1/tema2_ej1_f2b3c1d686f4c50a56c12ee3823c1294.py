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
        print("¿Qué figura geométrica deseas calcular?")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Rombo")
        print("4. Círculo")
        print("5. Salir")

        opcion = int(input("Ingresa el número de opción: "))

        if opcion == 1:
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            resultado = area_triangulo(base, altura)
            print("El área del triángulo es:", resultado)
        elif opcion == 2:
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            resultado = area_rectangulo(base, altura)
            print("El área del rectángulo es:", resultado)
        elif opcion == 3:
            diagonal1 = float(input("Ingresa la primera diagonal del rombo: "))
            diagonal2 = float(input("Ingresa la segunda diagonal del rombo: "))
            resultado = area_rombo(diagonal1, diagonal2)
            print("El área del rombo es:", resultado)
        elif opcion == 4:
            radio = float(input("Ingresa el radio del círculo: "))
            resultado = area_circulo(radio)
            print("El área del círculo es:", resultado)
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Por favor, ingresa un número válido.")
           