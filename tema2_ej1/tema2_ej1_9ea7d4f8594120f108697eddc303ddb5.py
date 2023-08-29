import math
def area_triangulo(base,altura):
  area = (base * altura)/2
  return area
def area_rectangulo(base,altura):
  area = (base * altura)
  return area

def area_rombo(diagonal1,diagonal2):
  area = (diagonal1 * diagonal2)/2
  return area

def area_circulo(radio):
  area = radio *  radio * math.pi
  return area

if __name__ == "__main__":
  tipo_area = int(input("Qué área desea calcular? 1.Triángulo 2.Rectángulo 3.Rombo 4.Circulo:"))
  if tipo_area == 1:
    base = int(input("Ingrese el valor de la base:"))
    altura = int(input("Ingrese el valor de la altura:"))
    print(area_triangulo(base,altura))
  if tipo_area == 2:
    base = int(input("Ingrese el valor de la base:"))
    altura = int(input("Ingrese el valor de la altura:"))
    print(area_rectangulo(base,altura))
  if tipo_area == 3:
    diagonal1 = int(input("Ingrese el valor de la diagonal1:"))
    diagonal2 = int(input("Ingrese el valor de la diagonal2:"))
    print(area_rombo(diagonal1,diagonal2))
  if tipo_area == 4:
    radio = int(input("Ingrese el valor del radio:"))
    print(area_circulo(radio))
           