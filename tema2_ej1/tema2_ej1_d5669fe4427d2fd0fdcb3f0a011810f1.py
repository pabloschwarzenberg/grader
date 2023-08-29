import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    while True:
        print("1. Calcular área de un rectángulo")
        print("2. Calcular área de un triángulo")
        print("3. Calcular área de un rombo")
        print("4. Calcular área de un círculo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == "2":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        elif opcion == "3":
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
            print("El área del rombo es:", area)
        elif opcion == "4":
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            import math

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

if __name__ == "__main__":
    base = 11
    altura = 7
    area_esperada = 38.5

    area_calculada = calcular_area_triangulo(base, altura)

    if area_calculada != area_esperada:
        print("¡Error! El área calculada no coincide con el valor esperado.")
    else:
        print("El área del triángulo es correcta: ", area_calculada)


