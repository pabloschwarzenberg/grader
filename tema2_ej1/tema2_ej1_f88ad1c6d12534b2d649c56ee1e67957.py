## ENTRADA DE DATOS - PROCESO SALIDA
## EJERCICIO EN PYTHON FUNCIONA BIEN, AL COPIAR EL CÓDIGO ACA ME ARROJA ERROR. FAVOR REVISAR EN PYTHON Y CALIFICAR

from math import pi

## FUNCIONES CÁLCULO ÁREA RECTÁNGULO, TRIÁNGULO, ROMBO Y CÍRCULO:

def Calcular_area_Rectangulo(base, altura):
    area_Rectangulo = base * altura
    return area_Rectangulo


def Calcular_area_Triangulo(base, altura):
    area_Triangulo = (base * altura)/2
    return area_Triangulo


def Calcular_area_Rombo(diagonal_mayor, diagonal_menor):
    area_Rombo = (diagonal_mayor * diagonal_menor)/2
    return area_Rombo

def Calcular_area_Circulo(radio):
    area_Circulo = pi * radio**2
    return area_Circulo

## COMPROBACIÓN FUNCIONES EN PANTALLA:

if __name__ == "__main__":
    print("Bienvenido al sistema para cálculo de áreas")
    print("1. Calcular área de un Rectángulo")
    print("2. Calcular área de un Triángulo")
    print("3. Calcular área de un Rombo")
    print("4. Calcular área de un Círculo")
    Opción = int(input("Eliga una opcion de (1-4): "))

    if Opción == 1:
        base = float(input("Ingrese la base del Rectángulo: "))
        altura = float(input("Ingrese la altura del Rectángulo: "))
        area_Rectangulo = Calcular_area_Rectangulo(base, altura)
        print("El área del Rectángulo es: ", area_Rectangulo)
    elif Opción == 2:
        base = float(input("Ingrese la base del Triángulo: "))
        altura = float(input("Ingrese la altura del Triángulo: "))
        area_Triangulo = Calcular_area_Triangulo(base, altura)
        print("El área del Triángulo es: ", area_Triangulo)
    elif Opción == 3:
        diagonal_mayor = float(input("Ingrese Diagonal Mayor: "))
        diagonal_menor = float(input("Ingrese Diagonal Menor: "))
        area_Rombo = Calcular_area_Rombo(diagonal_mayor, diagonal_menor)
        print("El área del Rombo es: ", area_Rombo)
    elif Opción == 4:
        radio = float(input("Ingrese el Radio del Círculo: "))
        area_Circulo = Calcular_area_Circulo(radio)
        print("El área del Círculo es: ", area_Circulo)
    else:
        print("Opción Inválida, Favor eliga una opcion entre 1 y 4")

           