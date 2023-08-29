import math
def area_triangulo(base,altura):
  formula_triangulo = (base*altura)/2
  return formula_triangulo
def area_rectangulo(base,altura):
  formula_rectangulo = (base*altura)
  return formula_rectangulo
def area_rombo(diagonal1,diagonal2):
  formula_rombo = (diagonal1*diagonal2)/2
  return formula_rombo
def area_circulo(radio):
  formula_circulo = (math.pi*(radio**2))
  return formula_circulo
opcion = 3
while (opcion !=5):
  print("elija su operación ")
  print("1) area triangulo")
  print("2) area rectangulo")
  print("3) area rombo")
  print("4) area ciculo")
  print("5) Cerrar")
  if opcion == 1:
    print(area_triangulo(base,altura))
  elif opcion == 2:
    print(area_rectangulo(base,altura))
  elif opcion == 3:
    print(area_rombo(diagonal1,diagonal2))
  elif opcion == 4:
    print(area_circulo(radio))
  elif opcion == 5:
    print("chao")