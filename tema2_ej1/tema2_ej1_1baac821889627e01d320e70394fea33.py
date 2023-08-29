import math

def area_triangulo(base, altura):
            return int(base) * int(altura) /2
        area= area_triangulo(base,altura)
        

def area_rectangulo(base, altura):
  return (base) * (altura)
  area= area_rectangulo(base,altura)

            
def area_circulo(radio):
  return math.pi * (radio)**2
  area= area_circulo(radio)


def area_rombo(diagonal1, diagonal2):
  return (diagonal1) * (diagonal2) / 2
  area= area_rombo(diagonal1, diagonal2)