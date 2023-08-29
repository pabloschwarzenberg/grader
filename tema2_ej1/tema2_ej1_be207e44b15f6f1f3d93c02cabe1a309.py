# Importar la constante pi de la librería math
from math import pi

# Definir una función que calcula el área de un rectángulo
def area_rectangulo(base, altura):
  # Retornar el producto de la base por la altura
  return base * altura

# Definir una función que calcula el área de un triángulo
def area_triangulo(base, altura):
  # Retornar la mitad del producto de la base por la altura
  return base * altura / 2

# Definir una función que calcula el área de un rombo
def area_rombo(diagonal_mayor, diagonal_menor):
  # Retornar la mitad del producto de las diagonales
  return diagonal_mayor * diagonal_menor / 2

# Definir una función que calcula el área de un círculo
def area_circulo(radio):
  # Retornar el producto de pi por el cuadrado del radio
  return pi * radio ** 2

# Si el programa se ejecuta como principal
if __name__ == "__main__":
  # Definir una variable para controlar si se desea continuar o no
  continuar = "S"
  # Mientras se desee continuar
  while continuar == "S":
    # Imprimir un menú con las opciones disponibles
    print("Menú:")
    print("1. Calcular el área de un rectángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rombo")
    print("4. Calcular el área de un círculo")
    print("5. Salir")
    # Pedir al usuario que ingrese una opción
    opcion = int(input("Ingresa una opción: "))
    # Si la opción es 1
    if opcion == 1:
      # Pedir al usuario que ingrese la base y la altura del rectángulo
      base = float(input("Ingresa la base del rectángulo: "))
      altura = float(input("Ingresa la altura del rectángulo: "))
      # Llamar a la función correspondiente y guardar el resultado
      area = area_rectangulo(base, altura)
      # Imprimir el resultado
      print("El área del rectángulo es", area)
    # Si la opción es 2
    elif opcion == 2:
      # Pedir al usuario que ingrese la base y la altura del triángulo
      base = float(input("Ingresa la base del triángulo: "))
      altura = float(input("Ingresa la altura del triángulo: "))
      # Llamar a la función correspondiente y guardar el resultado
      area = area_triangulo(base, altura)
      # Imprimir el resultado
      print("El área del triángulo es", area)
    # Si la opción es 3
    elif opcion == 3:
      # Pedir al usuario que ingrese las diagonales del rombo
      diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
      diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
      # Llamar a la función correspondiente y guardar el resultado
      area = area_rombo(diagonal_mayor, diagonal_menor)
      # Imprimir el resultado
      print("El área del rombo es", area)
    # Si la opción es 4
    elif opcion == 4:
      # Pedir al usuario que ingrese el radio del círculo
      radio = float(input("Ingresa el radio del círculo: "))
      # Llamar a la función correspondiente y guardar el resultado
      area = area_circulo(radio)
      # Imprimir el resultado
      print("El área del círculo es", area)
    # Si la opción es 5
    elif opcion == 5:
      # Cambiar la variable continuar a "N" para salir del ciclo
      continuar = "N"
    else:
      # Imprimir un mensaje de error indicando que la opción no es válida
      print("Opción no válida")
  
  print("Has salido")
