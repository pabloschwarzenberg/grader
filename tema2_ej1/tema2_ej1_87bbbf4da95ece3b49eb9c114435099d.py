import math
a = math.pi

def area_triangulo(base,altura):
    Areatri = (base * altura)/2
    return Areatri
def area_rectangulo(base,altura):
    areare = base * altura
    return areare
def area_rombo(diagonal1,diagonal2):
    AreaRo = (diagonal1 * diagonal2)/2
    return AreaRo
def area_circulo(radio):
    AreaCi = a * radio**2
    return AreaCi
if __name__ == "__main__":   
  BaTri = int(input("Ingrese Base del triangulo:"))
  AltTri = int(input("Ingrese Altura del triangulo:"))
  print(area_triangulo(BaTri, AltTri))
  BaRec = int(input("Ingrese Base del rectangulo:"))
  AltRec = int(input("Ingrese Altura del rectangulo:"))
  print(area_rectangulo(BaRec, AltRec))
  Dia1Rom = int(input("Ingrese diagonal 1 del rombo:"))
  Dia2Rom = int(input("Ingrese diagonal 2 del rombo:"))
  print(area_rombo(Dia1Rom, Dia2Rom))
  RadCir = int(input("Ingrese radio del Circulo:"))
  print(area_circulo(RadCir))
           