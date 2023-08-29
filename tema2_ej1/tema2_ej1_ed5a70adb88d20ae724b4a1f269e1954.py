import math
def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

def area_rectangulo(base,altura):
    area = base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area

def area_circulo(radio):
    area = math.pi * radio **2
    return area

if __name__ == "__main__":
    print("1. Triangulo\n2. Rectangulo\n3. Rombo\n4. Circulo")
    figura = int(input("Elija la forma que dese calcular su área: "))
    if figura == 1:
      base = float(input("Ingrese la medida de la Base: "))
      altura = float(input("Ingrese la medida de la Altura: "))
      area = area_triangulo(base, altura)
      print("El área es ", area)
    elif figura == 2:
      base = float(input("Ingrese la medida de la Base: "))
      altura = float(input("Ingrese la medida de la Altura: "))
      area = area_rectangulo(base, altura)
      print("El área es ", area)
    elif figura == 3:
      diagonal1 = float(input("Ingrese la medida de la primera diagonal: "))
      diagonal2 = float(input("Ingrese la medida de la segunda diagonal: "))
      area = area_rombo(diagonal1,diagonal2)
      print("El área es ", area)
    elif figura == 4:
      radio = float(input("Ingrese la medida del radio"))
      area = area_circulo(radio)
      print("El área es ", area)
    else:
      print("Opcion inválida")