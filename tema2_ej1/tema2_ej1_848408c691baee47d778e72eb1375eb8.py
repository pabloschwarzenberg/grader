from math import pi


def area_triangulo(base, altura):
     return (base * altura) / 2


def area_rectangulo(base, altura):
     return base * altura


def area_rombo(diagonal1, diagonal2):
     return (diagonal1 * diagonal2) / 2


def area_circulo(radio):
     return pi * radio ** 2


if __name__ == "__main__":
     opcion = int(input("""
 1 - Área del rectángulo
 2 - Área del triángulo
 3 - Área del rombo
 4 - Área del círculo
 Ingrese su elección:
#     """))
     if opcion == 1:
         base = int(input("ingrese el valor base: "))
         altura = int(input("ingrese el valor de la altura: "))

         print("El área del rectángulo:", area_rectangulo(base, altura))
     elif opcion == 2:
         base = int(input("ingrese el valor base: "))
         altura = int(input("ingrese el valor de la altura: "))

         print("El área del triangulo:", area_triangulo(base, altura))

     elif opcion == 3:
         diagonal1 = int(input("ingrese el valor de la diagonal1: "))
         diagonal2 = int(input("iingrese el valor de la diagona2: "))

         print("El área del rombo:", area_rombo(diagonal1, diagonal2))

     elif opcion == 4:
         radio = int(input("ingrese el radio del círculo: "))
         print("El área del círculo:", area_circulo(radio))
     else:
         print("entrada incorrecta. corre de nuevo")