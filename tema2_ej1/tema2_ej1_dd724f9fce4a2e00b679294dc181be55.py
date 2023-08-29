import math

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    print("Seleccione la figura para calcular el área:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        resultado = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es: {resultado}")
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        resultado = calcular_area_triangulo(base, altura)
        print("El área del triángulo es: {resultado}")
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        resultado = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es: {resultado}")
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = calcular_area_circulo(radio)
        print("El área del círculo es: {resultado}")
    else:
        print("Opción inválida")
           