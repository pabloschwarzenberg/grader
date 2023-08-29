def area_triangulo(base,altura):
    area=base*altura/2
    return area
def area_rectangulo(base,altura):
    area=base*altura
    return area
def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    return area
def area_circulo(radio):
    import math
    area=math.pi*radio**2
    return area

if __name__ == "__main__":
  print("a) calcular area triangulo")
  print("b) calcular area rectangulo")
  print("c) calcular area rombo")
  print("d) calcular area circulo")
  a=input("que desea hacer?: ")
  if a=="a":
      base=float(input("ingrese base: "))
      altura=float(input("ingrese altura: "))
      print(area_triangulo(base,altura))
  elif a=="b":
      base=float(input("ingrese base: "))
      altura=float(input("ingrese altura: "))
      print(area_rectangulo(base,altura))
  elif a=="c":
      diagonal1=float(input("ingrese diagonal1: "))
      diagonal2=float(input("ingrese diagonal2: "))
      print(area_rombo(diagonal1,diagonal2))
  elif a=="d":
      radio=float(input("ingrese radio: "))
      print(area_circulo(radio))
           