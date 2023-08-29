import math
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
    area=math.pi*(radio)**2
    return area
if __name__ == "__main__":
  figura=int(input("Area de: [1:Triangulo] [2:Rectangulo] [3:Rombo] [4:Circulo](Ingresar el número,1,2,3 o 4)"))
  if figura == 1:
        base=float(input("Ingrese base: "))
        altura=float(input("Ingrese altura: "))
        area=area_triangulo(base,altura)
  elif figura==2:
      base=float(input("Ingrese base: "))
      altura=float(input("Ingrese altura: "))
      area=area_rectangulo(base,altura)
  elif figura==3:
      diagonal1=float(input("Ingrese diagonal 1: "))
      diagonal2=float(input("Ingrese diagonal 2: "))
      area=area_rombo(diagonal1,diagonal2)
  elif figura==4:
      radio=float(input("Ingrese radio: "))
      area=area_circulo(radio)
  else:
      print("Opción no válida")
      exit()
  print("El area de su figura es:",area)
                       