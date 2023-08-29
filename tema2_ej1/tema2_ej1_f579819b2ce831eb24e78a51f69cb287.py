def area_triangulo(base,altura):
  base = float(base)
  altura = float(altura)
  area = (base*altura)/2
  return area

def area_rectangulo(base,altura):
  base = float(base)
  altura = float(altura)
  area = base*altura
  return area

def area_rombo(diagonal1,diagonal2):
  diagonal1 = float(diagonal1)
  diagonal2 = float(diagonal2)
  area = (diagonal1*diagonal2)/2
  return area

def area_circulo(radio):
  radio = float(radio)
  pi = 3.1415926535897932
  area = pi*(radio*radio)
  return area
           