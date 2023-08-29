def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base * altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1*diagonal2)/2

def area_circulo(radio):
    return pi* (radio)**2
import math
pi = math.pi

if __name__ == "__main__": 
  while True:
      print("\n---- Menú Principal ----")
      print("1. Área del Triángulo")
      print("2. Área del Rectángulo")
      print("3. Área del Rombo")
      print("4. Área del Círculo")
      print("5. Salir")

      op_menu = int(input("Ingrese una opción del menú: "))

      if (op_menu == 1):
          base = float(input("Ingrese la base del triángulo: "))
          altura = float(input("Ingrese la altura del triángulo: "))
          area = area_triangulo(base,altura)
          print("El área del triángulo de base", round(base,2),"y altura", round(altura,2),"es ", round(area,2))
      elif (op_menu == 2):
          base = float(input("Ingrese la base del rectángulo: "))
          altura = float(input("Ingrese la altura del rectángulo: "))
          area = area_rectangulo(base, altura)
          print("El área del rectángulo de base", round(base,2),"y altura", round(altura,2),"es ", round(area,2))
      elif (op_menu == 3):
          diagonal1 = float(input("Ingrese la primera diagonal del rombo: "))
          diagonal2 = float(input("Ingrese la segunda diagonal del rombo: "))
          area = area_rombo(diagonal1, diagonal2)
          print("El área del rombo de diagonales", round(diagonal1,2),"y ", round(diagonal2,2),"es ", round(area,2))
      elif (op_menu == 4):
          radio = float(input("Ingrese el radio del círculo: "))
          area =area_circulo(radio)
          print("El área del círculo de radio", round(radio,2),"es ",round(area,2))
      elif (op_menu == 5):
          break
  print ("Saliste del programa")   