import math
from math import pi

def area_triangulo(base,altura):
  a=(base*altura)/2
  return a


def area_rectangulo(base,altura):
  a=base*altura
  return a
    

def area_rombo(diagonal1,diagonal2):
  a=(diagonal1*diagonal2)/2
  return a
    

def area_circulo(radio):
  a=pi*(radio*radio)
  return a
    

if __name__ == "__main__":
  print("menu")
  print("1-area triangulo")
  print("2-area rectangulo")
  print("3-area rombo")
  print("4-area circulo")
  h=int(input("escoja area a calcular: "))
  if h==1:
    altura=int(input("altura: "))
    base=int(input("base: "))
    print(area_triangulo(base,altura))
  elif h==2:
    altura=int(input("altura: "))
    base=int(input("base: "))
    print(area_rectangulo(base,altura))
  elif h==3:
    diagonal1=int(input("diagonal1: "))
    diagonal2=int(input("diagonal2: "))
    print(area_rombo(diagonal1,diagonal2))
  elif h==4:
    radio=float(input("radio: "))
    print(area_circulo(radio))
  
           