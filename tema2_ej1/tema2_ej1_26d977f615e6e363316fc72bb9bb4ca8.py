def area_triangulo(base,altura):
    area=(base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
  from math import pi
  area=(radio**2)*pi
  return area
    

if __name__ == "__main__":
  b=float(input())
  h=float(input())
  d1=float(input())
  d2=float(input())
  r=float(input())
  print(area_triangulo(b,h))
  print(area_rectangulo(b,h))
  print(area_rombo(d1,d2))
  print(area_circulo(r))
  
           