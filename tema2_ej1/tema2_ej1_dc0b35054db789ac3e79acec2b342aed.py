# Importar la constante pi de la librería math
from math import pi

# Definir una función que calcule el área de un rectángulo
def area_rectangulo(base, altura):
    # El área del rectángulo es el producto de la base por la altura
    return base * altura

# Definir una función que calcule el área de un triángulo
def area_triangulo(base, altura):
    # El área del triángulo es la mitad del producto de la base por la altura
    return base * altura / 2

# Definir una función que calcule el área de un rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    # El área del rombo es la mitad del producto de las diagonales
    return diagonal_mayor * diagonal_menor / 2

# Definir una función que calcule el área de un círculo
def area_circulo(radio):
    # El área del círculo es el producto de pi por el cuadrado del radio
    return pi * radio ** 2

# Definir una función que muestre un menú con las opciones de cálculo
def menu():
    # Imprimir las opciones
    print("Bienvenido al programa de cálculo de áreas.")
    print("1. Calcular el área de un rectángulo.")
    print("2. Calcular el área de un triángulo.")
    print("3. Calcular el área de un rombo.")
    print("4. Calcular el área de un círculo.")
    print("5. Salir del programa.")
    # Pedir al usuario que ingrese una opción
    opcion = int(input("Ingrese una opción: "))
    # Retornar la opción elegida
    return opcion

# Probar el programa con un ciclo que se repita hasta que el usuario quiera salir
if __name__ == "__main__":
    # Inicializar la opción con 0
    opcion = 0
    # Repetir mientras la opción no sea 5 (salir)
    while opcion != 5:
        # Mostrar el menú y obtener la opción elegida
        opcion = menu()
        # Si la opción es 1, calcular el área de un rectángulo
        if opcion == 1:
            # Pedir al usuario que ingrese la base y la altura del rectángulo
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            # Calcular el área usando la función correspondiente
            area = area_rectangulo(base, altura)
            # Imprimir el resultado
            print("El área del rectángulo es", area)
        # Si la opción es 2, calcular el área de un triángulo
        elif opcion == 2:
            # Pedir al usuario que ingrese la base y la altura del triángulo
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            # Calcular el área usando la función correspondiente
            area = area_triangulo(base, altura)
            # Imprimir el resultado
            print("El área del triángulo es", area)
        # Si la opción es 3, calcular el área de un rombo
        elif opcion == 3:
            # Pedir al usuario que ingrese las diagonales del rombo
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            # Calcular el área usando la función correspondiente
            area = area_rombo(diagonal_mayor, diagonal_menor)
            # Imprimir el resultado
            print("El área del rombo es", area)
        # Si la opción es 4, calcular el área de un círculo
        elif opcion == 4:
            # Pedir al usuario que ingrese el radio del círculo
            radio = float(input("Ingrese el radio del círculo: "))
            # Calcular el área usando la función correspondiente
            area = area_circulo(radio)
            # Imprimir el resultado
            print("El área del círculo es",area)
        # Si la opción es 5, salir del programa
        elif opcion == 5:
            print("Gracias por usar el programa. Adiós.")
        # Si la opción no es válida, mostrar un mensaje de error
        else:
            print("Opción inválida. Intente de nuevo.")
           