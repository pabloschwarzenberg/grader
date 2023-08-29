import math
def area_triangulo(base,altura):
    areatriangulo=base*altura/2
    return areatriangulo
def area_rectangulo(base,altura):
    arearectangulo=base*altura
    return arearectangulo
def area_rombo(diagonal1,diagonal2):
    arearombo=diagonal1*diagonal2/2
    return arearombo
def area_circulo(radio):
    areacirculo=math.pi*radio*radio
    return areacirculo
if __name__ == "__main__":
  print("""Eliga la figura que quiera calcular su area
  (1) Triangulo
  (2) rectangulo
  (3) Rombo
  (4) Circulo""")
  x=input("Ingrese el numero con la opcion que desea realizar: ")

  if x=="1":
      base=int(input("Ingrese la base del triangulo: "))
      altura=int(input("Ingrese la altura del triangulo: "))
      print(area_triangulo(base,altura))
  elif x=="2":
      base=int(input("Ingrese la base del rectangulo: "))
      altura=int(input("Ingrese la altura del rectangulo: "))
      print(area_rectangulo(base,altura))   
  elif x=="3":
      diagonal1=int(input("Ingrese la diagonal 1 del rombo: "))
      diagonal2=int(input("Ingrese la diagonal 2 del rombo: "))
      print(area_rombo(diagonal1,diagonal2))
  elif x=="4":
      radio=int(input("Ingrese el radio del circulo: "))
      print(area_circulo(radio))

           