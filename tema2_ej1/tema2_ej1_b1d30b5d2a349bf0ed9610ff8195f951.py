from math import pi
def area_triangulo(base,altura):
  area=(base*altura)/2
  return (area)
def area_rectangulo(base,altura):
  area=(base*altura)
  return (area)
def area_rombo(diagonal1,diagonal2):
  area=(diagonal1*diagonal2)/2
  return (area)
def area_circulo(radio):
  area=(pi*radio**2)
  return (area)
print("CALCULADORA GEOMETRICA")
print("Elige una opción")
print("1-Area Triangular")
print("2-Area Rectangular")
print("3-Area del Rombo")
print("4-Area Circular")
print("0-SALIDA")
  opciones = int(input("Escribe tu elección: "))
  if(opciones==0):
    print("Hasta la proxima")
  elif(opciones==1):
    base=float(input("Ingrese base: "))
    altura=float(input("Ingrese altura: "))
    print(area_triangulo(base,altura))
  elif(opciones==2):
      base=float(input("Ingrese base: "))
      altura=float(input("Ingrese altura: "))
      print(area_rectangulo(base,altura))
  elif(opciones==3):
      diagonal1=float(input("Ingrese diagonal uno: "))
      diagonal2=float(input("Ingrese diagonal dos: "))
      print(area_rombo(diagonal1,diagonal2))
  elif(opciones==4):
      radio=float(input("Ingrese el radio: "))
      print(area_circulo(radio))
  else:
      print("Numero invalido")