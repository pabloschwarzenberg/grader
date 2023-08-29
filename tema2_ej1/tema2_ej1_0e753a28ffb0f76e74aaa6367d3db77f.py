def area_triangulo(base,altura):
  area=(base*altura)/2
  return area

def area_rectangulo(base,altura):
  area=base*altura
  return area

def area_rombo(diagonal1,diagonal2):
  area=(diagonal1 * diagonal2)/2
  return area
def area_circulo(radio):
  pi=3.141592653589793
  area= pi*radio*radio
  return area

#__name__ = input("ingrese menú")

if __name__ == "area_triangulo":
  base=eval(input("ingrese base"))
  altura=eval(input("ingrese altura"))
  print(area_triangulo)
if __name__=="area_rectangulo":
  base=eval(input("ingrese base"))
  altura=eval(input("ingrese altura"))
  area_rectangulo(base,altura)
  print(area_rectangulo)
if __name__=="area_rombo":
  diagonal1=eval(input("ingrese diagonal 1"))
  diagonal2=eval(input("ingrese diagonal 2"))
  print(area_rombo(diagonal1,diagonal2))
if __name__=="area_circulo":
  radio=eval(input("ingrese radio"))
  print(area_circulo(radio))
