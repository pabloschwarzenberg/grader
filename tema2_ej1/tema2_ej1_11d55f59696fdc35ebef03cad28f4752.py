import math
def area_triangulo(base,altura):
  x = (base * altura)/2
  return x
  pass

def area_rectangulo(base,altura):
  x = base * altura
  return x
  pass

def area_rombo(diagonal1,diagonal2):
  x = (diagonal1 * diagonal2)/2
  return x
  pass

def area_circulo(radio):
  x = math.pi * (radio * radio)
  return x
  pass

if __name__ == "__main__":
  a=int(input("1)Triangulo  2)Rectangulo  3)Rombo  4)Circulo"))
  if a == 1:
    x = eval(input())
    y = eval(input())
    print(area_triangulo(x,y))
  if a == 2:
    x = eval(input())
    y = eval(input())
    print(area_rectangulo(x,y))
  if a == 3:
    x = eval(input())
    y = eval(input())
    print(area_rombo(x,y))
  if a == 4:
    x = eval(input())
    print(area_circulo(x))
  pass
           