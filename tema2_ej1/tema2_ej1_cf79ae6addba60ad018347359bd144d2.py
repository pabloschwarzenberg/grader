import math
def area_triangulo(base,altura):
    area=(base*altura)/2
    return area
def area_rectangulo(base,altura):
    area=(base*altura)
    return area
def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area=(radio**2)*math.pi
    return area
if __name__ == "__main__":
    while True:
      print("Elija una opcion")
      print("1)Calcular el area de un triangulo")
      print("2)Calcular el area de un rectangulo")
      print("3)Calcular el area de un circulo")
      print("4)Calcular el area de un rombo")
      print("5)Apagar")
      t=int(input())
      if t==1:
          a=float(input("Ingrese la base del triangulo: "))
          b=float(input("Ingrese la altura del triangulo: "))
          print(area_triangulo(a,b))
      elif t==2:
          c=float(input("Ingrese la base del rectangulo: "))
          d=float(input("Ingrese la altura del rectangulo: "))
          print(area_rectangulo(c,d))
      elif t==3:
          e=float(input("Ingrese el radio del circulo: "))
          print(area_circulo(e))
      elif t==4:  
          f=float(input("Ingrese la diagonal del rombo: "))
          g=float(input("Ingrese la otra diagonal del rombo: "))
          print(area_rombo(f,g))
      elif t==5:
          break