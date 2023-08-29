import math
def area_triangulo(base,altura):
  areaTriangulo=(base*altura)/2
  return areaTriangulo
  pass

def area_rectangulo(base,altura):
  areaRectangulo=base*altura
  return areaRectangulo
  pass

def area_rombo(diagonal1,diagonal2):
  areaRombo=(diagonal1*diagonal2)/2
  return areaRombo
  pass

def area_circulo(radio):
  radioCua=radio**2
  areaCirculo=math.pi*radioCua
  return areaCirculo
  pass


if __name__ == "__main__":
  eleccion=True
  while eleccion>=1 and eleccion<=4:
    eleccion=int(input("Que area desea calcular: [1: TRIANGULO][2: RECTANGULO][3: ROMBO][4: CIRCULO] "))
    if eleccion==1:
      base=int(input("Ingrese base: "))
      altura=int(input("Ingrese altura: "))
      print(area_triangulo(base,altura))
    elif eleccion==2:
      base=int(input("Ingrese base: "))
      altura=int(input("Ingrese altura: "))
      print(area_rectangulo(base,altura))
    elif eleccion==3:
      diagonal1=int(input("Ingrese diagonal mayor: "))
      diagonal2=int(input("Ingrese diagonal menor: "))
      print(area_rombo(diagonal1,diagonal2))
    elif eleccion==4:
      radio=float(input("Ingrese radio: "))
      print(area_circulo(radio))
    else:
      print("Alternativa no existente")