import math
def area_triangulo(base,altura):
  return (base*altura)/2
  
def area_rectangulo(base,altura):
  return base*altura
    

def area_rombo(diagonal1,diagonal2):
  return (diagonal1*diagonal2)/2
 

def area_circulo(radio):
  return math.pi*radio**2
    

if __name__ == "__main__":
  x = input("Que desea calcular:")
  if x==area_triangulo(base,altura):
    base = int(input())
    altura = int(input())
  elif x==area_rectangulo(base,altura):
    base = int(input())
    altura = int(input())
  elif x==area_rombo(diagonal1,diagonal2):
    diagonal1 = int(input())
    diagonal2 = int(input())
  elif x==area_circulo(radio):
    radio = int(input())
  else: 
    pass
        
           