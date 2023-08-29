import math
def area_rectangulo(base, altura):
    return base * altura
def area_triangulo(base, altura):
    return (base * altura) / 2
def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2
def area_circulo(radio):
    return math.pi * radio ** 2
if __name__ == "__main__":
    print("Cálculo de áreas")
    print("----------------")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    opcion = int(input("Seleccione una opción (1-4): "))
    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        print("El área del rectángulo es:", resultado)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        print("El área del triángulo es:", resultado)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        resultado = area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", resultado)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = area_circulo(radio)
        print("El área del círculo es:", resultado)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del 1 al 4.")
           

#NUMNEROS PERFECTOS
def numero_perfecto(numero):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == numero
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")