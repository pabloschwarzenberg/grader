import math
def area_triangulo(base,altura):
  area=(base*altura)/2
  return area
def area_rectangulo(base,altura):
  area=base*altura
  return area
def area_rombo(diagonal1,diagonal2):
  area=(diagonal1*diagonal2)/2
  return area
def area_circulo(radio):
  area=math.pi*(radio)**2
  return area
if __name__ == "__main__":
    print("Selecciona el area que queires calcular:")
    print("1.Triangulo")
    print("2.Rectangulo")
    print("3.Rombo")
    print("4.Circulo")
    fig=int(input())
    if fig==1 or fig==2:
      print("Ingresa la base y la altura:")
      base=int(input())
      altura=int(input())
      if fig==1:
        area=area_triangulo(base,altura)
        print("El area del triangulo es",area)
      elif fig==2:
        area=area_rectangulo(base,altura)
        print("El area del rectangulo es",area)
    elif fig==3:
      print("Ingresa las diagonales:")
      diag1=int(input())
      diag2=int(input())
      area=area_rombo(diag1,diag2)
      print("El area del rombo es",area)
    elif fig==4:
      print("Ingresa el radio:")
      radio=float(input())
      area=area_circulo(radio)
      print("El area del circulo es",area)     