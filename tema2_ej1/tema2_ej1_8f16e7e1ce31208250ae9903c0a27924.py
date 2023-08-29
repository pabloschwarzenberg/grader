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
    while True:
        print("Seleccione la figura geométrica para calcular su área:")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Rombo")
        print("4. Círculo")
        opcion = int(input("Ingrese opción (1-4): "))
        if opcion == 1:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            resultado = area_rectangulo(base, altura)
            print("El área del rectángulo es:", resultado)
            break
        elif opcion == 2:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            resultado = area_triangulo(base, altura)
            print("El área del triángulo es:", resultado)
            break
        elif opcion == 3:
            diagonal_mayor = float(input("Ingrese la diagonal mayor: "))
            diagonal_menor = float(input("Ingrese la diagonal menor: "))
            resultado = area_rombo(diagonal_mayor, diagonal_menor)
            print("El área del rombo es:", resultado)
            break
        elif opcion == 4:
            radio = float(input("Ingrese el radio: "))
            resultado = area_circulo(radio)
            print("El área del círculo es:", resultado)
            break
        else:
            print("Opción inválida, por favor seleccione entre 1 y 4.")


         