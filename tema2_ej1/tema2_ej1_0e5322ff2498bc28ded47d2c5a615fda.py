import math

def area_triangulo(base, altura):
  area=(base * altura)/2
  return print("El area de un triangulo es:",area)

def area_rectangulo(base,altura):
  area=(base * altura)
  return print("El area es:",area)

def area_rombo(diagonal1,diagonal2):
  area=(diagonal1 * diagonal2)/2
  return print("El area es:",area)

def area_circulo(radio):
  area=(math.pi * radio**2)
  return print("El area es:",area)
  
if __name__ == "__main__":
  print ("""
Menu

1) Área triangulo

2) Área rectangulo

3) Área rombo

4) Área circulo""")
  menu=int(input("Seleccione su opcion: "))
  if menu>0 and menu<=3:
    base=int(input("Ingrese su base: "))
    altura=int(input("Ingrese su altura: "))
    if menu==1:
      area_triangulo(base,altura)
    elif menu==2:
      area_rectangulo(base,altura)
  elif menu==3:
    diagonal1=int(input("Ingrese su primer diagonal: "))
    diagonal2=int(input("Ingrese su segundo diagonal: "))
    area_rombo(diagonal1,diagonal2)              
  elif menu==4:
    radio=int(input("ingrese su Radio: "))