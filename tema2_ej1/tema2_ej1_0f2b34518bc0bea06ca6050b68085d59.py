import math
pi = math.pi
def area_triangulo(base,altura):
  area_triangulo = (base*altura)*1/2
  return area_triangulo

def area_rectangulo(base,altura):
  area_rectangulo = (base*altura)
  return area_rectangulo

def area_rombo(diagonal1,diagonal2):
  area_rombo = (diagonal1*diagonal2)*1/2
  return area_rombo

def area_circulo(radio):
  area_circunferencia = (pi*radio*radio)
  return area_circunferencia

print("1. Area Triangulo")
print("2. Area Rectangulo")
print("3. Area Rombo")
print("3. Area Circulo")  

