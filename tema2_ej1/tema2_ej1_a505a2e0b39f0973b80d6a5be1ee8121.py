import math

def area_triangulo(base,altura):
  r=(base*altura)/2
  return r
def area_rectangulo(base,altura):
  r=base*altura
  return r
def area_rombo(diagonal1,diagonal2):
  r=(diagonal1*diagonal2)/2
  return r
def area_circulo(radio):
  r=math.pi*(radio**2)
  return r

if __name__ == "__main__":
  base1=int(input())
  altura1=int(input())
  print(area_triangulo(base1,altura1))
  base2=int(input())
  altura2=int(input())
  print(area_rectangulo(base2,altura2))
  diagonal1=int(input())
  diagonal2=int(input())
  print(area_rombo(diagonal1,diagonal2))
  radio=int(input())
  print(area_circulo(radio))
           