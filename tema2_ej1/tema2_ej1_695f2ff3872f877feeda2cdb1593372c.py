def area_triangulo(base,altura):
  area= (base*altura)/2
  return area
  
def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_circulo(radio):
  from math import pi
  area= (pi*(radio**2))           
  return area

def area_rombo(diagonal1,diagonal2):
  area= (diagonal1*diagonal2)/2
  return area
    
def calcular_areas():
  print("Que desea calcular?")
  print("1: Area triangulo, 2: Area rectangulo, 3:area circulo, 4:area rombo")
  opcion=int(input())

  if opcion == 1:
    area_triangulo()
  elif opcion == 2:
    area_rectangulo()
  elif opcion==3:
    area_circulo()
  elif opcion==4:
    area_rombo()
  return
    
