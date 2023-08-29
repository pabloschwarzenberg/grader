import math
def area_triangulo(base,altura):
    return (base * altura) / 2

def area_rectangulo(base,altura):
    return base * altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2) / 2

def area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    print("Bienvenido a la calculadora geometrica")
    print("triangulo")
    print("rectangulo")
    print("rombo")
    print("circulo")
    opcion = int(input("Ingresa el nombre de la figura que deseas calcular: "))
    
    if opcion == triangulo:
      base = float(input("Ingresa la medida de la base: "))
      altura = float(input("Ingresa la medida de la altura: "))
      area = area_triangulo(base, altura)
      print("El area del triangulo es", area)
      
    elif opcion == rectangulo:
      base = float(input("Ingrese la medida de la base: "))
      altura = float(input("Ingrese la medida de la altura: "))
      area = area_rectangulo(base, altura)
      print("El area del rectangulo es", area)
      
    elif opcion == rombo:
      diagonal1 = float(input("Ingrese la medida de la diagonal 1: "))
      diagonal2 = float(input("Ingrese la medida de la diagonal 2: "))
      area = area_rombo(diagonal1, diagonal2)
      print("El area del rombo es",area)
     
    elif opcion == circulo:
      radio = float(input("Ingrese la medida del radio: "))
      area = area_circulo(radio)
      print("El area del circulo es",area)
     
    else:
      print("Opcion invalida. Porfavor ingrese una de las 4 opciones")
           