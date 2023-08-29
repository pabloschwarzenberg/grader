import math

def arearectangulo(base, altura):
  return base * altura

def areatriangulo(base1, altura1):
  return (base1 * altura1) / 2

def arearombo(diagonal_mayor, diagonal_menor):
  return (diagonal_mayor * diagonal_menor) / 2

def areacirculo(radio):
  return math.pi * radio ** 2

if __name__ == "__main__":
  print("Programa de calculo de areas.")
  print("1. Rectangulo")
  print("2. Triangulo")
  print("3. Rombo")
  print("4. Circulo")
  opcion = int(input("Seleccione la figura para calcular su área (1-4): "))

if opcion == 1:
  base = float(input("Ingrese la base del rectángulo: "))
  altura = float(input("Ingrese la altura del rectángulo: "))
  area = arearectangulo(base, altura)
  print("El área del rectángulo es:", area)
if opcion == 2:
  base1 = float(input("Ingrese la base del triángulo: "))
  altura1 = float(input("Ingrese la altura del triángulo: "))
  area1 = areatriangulo(base, altura)
  print("El área del triángulo es:", area1)
if opcion == 3:
  diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
  diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
  area = arearombo(diagonal_mayor, diagonal_menor)
  print("El área del rombo es:", area)
if opcion == 4:
  radio = float(input("Ingrese el radio del círculo: "))
  area = areacirculo(radio)
  print("El área del círculo es:", area)
else:
  print("Opción inválida. Seleccione una opción del 1 al 4.")
