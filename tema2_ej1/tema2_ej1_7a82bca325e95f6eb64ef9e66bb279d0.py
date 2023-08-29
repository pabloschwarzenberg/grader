import math
p = math.pi
def area_triangulo(base,altura):
  area = (base*altura)/2
  return area
  pass

def area_rectangulo(base,altura):
  area = base * altura  
  return area 
  pass

def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)//2
    return area
    pass

def area_circulo(radio):
    area = p * radio**2
    return area
    pass

if __name__ == "__main__":
  numero = int(input())
  if numero == 1:
    base = int(input())
    altura = int(input())
    print(area_triangulo(base,altura))
  elif numero == 2:
    base = int(input())
    altura = int(input())
    print(area_rectangulo(base,altura))
  elif numero == 3:
    diagonal1 = int(input())
    diagonal2 = int(input())
    print(area_rombo(diagonal1,diagonal2))
  elif numero == 4:
    radio = int(input())
    print(area_circulo(radio))
           