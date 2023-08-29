import math as m
def area_triangulo(base,altura):
  area_triangulo= float(base * altura)/2
  return area_triangulo


def area_rectangulo(base,altura):
  area_rectangulo= float(base * altura)
  return area_rectangulo


def area_rombo(diagonal1,diagonal2):
  area_rombo= float(diagonal1 * diagonal2)/2
  return area_rombo


def area_circulo(radio):
  area_circulo= float(m.pi*(radio**2))
  return area_circulo
[07-07 17:10] Javier Flores UNAB: def suma_divisores(a):
  listaA = []
  for i in range(1,a):
    if a % i == 0:
      listaA.append(i)
  if sum(listaA) == 1:
    primo = True
  else:
    primo = False
  return sum(listaA),primo