import math
def area_triangulo(base,altura):
  n = (base * altura)/2
  return (n)

def area_rectangulo(base,altura):
  n = base * altura
  return (n)

def area_rombo(diagonal1,diagonal2):
  n = (diagonal1 * diagonal2)/2
  return (n)

def area_circulo(radio):
  n = math.pi * radio * radio
  return (n)

if __name__ == "__main__":
  rectangulo = 0
  circulo = 0
  rombo = 0
  triangulo = 0
  c = input("Ingrese figura geometrica (rectangulo, triangulo, rombo, circulo): ")
  if c == rectangulo:
    base = int(input("Ingrese base: "))
    altura = int(input("Ingrese altura: "))
    g = area_rectangulo(base,altura)
    print(g)
    
  elif c == triangulo:
    base = int(input("Ingrese base: "))
    altura = int(input("Ingrese altura: "))
    g = area_triangulo(base,altura)
    print(g)
    
  elif c == rombo:
    diagonal1 = int(input("Ingrese diagonal1: "))
    diagonal2 = int(input("Ingrese diagonal2: "))
    g = area_rombo(diagonal1,diagonal2)
    print(g)
    
  elif c == circulo:
    radio = int(input("Ingrese radio: "))
    g = area_rombo(diagonal1,diagonal2)
    print(g)