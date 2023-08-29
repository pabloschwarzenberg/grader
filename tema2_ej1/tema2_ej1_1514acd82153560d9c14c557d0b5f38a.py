from math import pi

def area_triangulo(base,altura):
    return (base * altura)/2

def area_rectangulo(base, altura):
    return base * altura

def area_rombo(diagonal11, diagonal12):
    return (diagonal11 * diagonal12)/2

def area_circulo(radio):
    return pi * radio**2
    
if __name__=="__main__":
  print(area_triangulo(5,7))
  print(area_rectangulo(3,5))
  print(area_rombo(7,9))
  print(area_circulo(6))
    