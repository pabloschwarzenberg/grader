from math import pi
def area_rectangulo(base1, altura1):
    return base1 * altura1

def area_triangulo(base2, altura2):
    return (base2 * altura2) / 2

def area_rombo(diagonal1, diagonal2):
    return (diagonal1*diagonal2)/2
    
def area_circulo(radio):
    return pi*(radio**2)

if __name__ == "__main__":
  print("Menu de Opciones")
  print("1. Para calcular el Area de un Rectangulo")
  print("2. Para calcular el Area de un Triangulo")
  print("3. Para calcular el Area de un Rombo")
  print("4. Para calcular el Area de un Circulo")
  op = int(input("Ingrese su opcion: "))
  if op == 1:
      base_r = float(input("Ingrese la base del rectangulo: "))
      altura_r = float(input("Ingrese la altura del rectangulo: "))
      print("El area del Rectangulo es: ", area_rectangulo(base_r, altura_r))
  elif op == 2:
      base_t = float(input("Ingrese la base del triangulo: "))
      altura_t = float(input("Ingrese la altura del triangulo: "))
      print("El area del Triangulo es: ", area_triangulo(base_t, altura_t))
  elif op == 3:
      D = float(input("Ingrese la Diagonal Principal: "))
      d = float(input("Ingrese la Diagonal Secundaria: "))
      print("El area del Rombo es: ", area_rombo(D, d))
  elif op == 4:
      radio = float(input("Ingrese el Radio del Circulo: "))
      print("El area del Circulo es: ", area_circulo(radio))

       