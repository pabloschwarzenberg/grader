from math import pi
def area_triangulo(base,altura):
    a = (base*altura)/2
    return a

def area_rectangulo(base,altura):
    a = (base*altura)
    return a

def area_rombo(diagonal1,diagonal2):
    a = (diagonal1 * diagonal2)/2
    return a 

def area_circulo(radio):
    a = pi * (pow(radio,2))
    return a

if __name__ == "__main__":
  figura = input("Indique que figra decea calcular:")
  if figura == "triangulo":
    base = int(input("ingrese la base"))
    altura = int(input("ingrese la altura"))
    area_triangulo(base,altura)
  elif figura == "rectangulo":
    base = int(input("ingrese la base"))
    altura = int(input("ingrese la altura"))
    area_rectangulo(base,altura)
  if figura == "rombo":
    d1 = int(input("ingrese la diagonal 1"))
    d2 = int(input("ingrese la diagonal 2"))
    area_rombo(d1,d2)
  if figura == "circulo":
    radio = int(input("ingrese el radio"))
    area_circulo(radio)