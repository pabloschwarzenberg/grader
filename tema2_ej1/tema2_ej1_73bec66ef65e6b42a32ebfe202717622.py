import math

def area_triangulo(base,altura):
    area=base*altura/2
    j=area
    return j

def area_rectangulo(base,altura):
    area=base*altura
    j=area
    return j

def area_rombo(diagonal1,diagonal2):
    area=diagonal1*diagonal2/2
    j=area
    return j

def area_circulo(radio):
    area=math.pi*radio**2
    j=area
    return j

if __name__ == "__main__":
    print("""
¿Que area quiere calcular?
(1) Triangulo
(2) Rectángulo o Cuadrado
(3) Rombo
(4) Circulo""")
    i=0
    i2=0
    while i==0:
      if i2==1:
        print("""
¿Que area quiere calcular?
(1) Triangulo
(2) Rectángulo o Cuadrado
(3) Rombo
(4) Circulo""")
      a=int(input("Seleccione una opción: "))
      if a==1 or a==2:
          x=float(input("Indique la base de la figura:"))
          h=float(input("Indique la altura de la figura: "))
          if a==1:
              print(area_triangulo(x,h))
          else:
              print(area_rectangulo(x,h))
      elif a==3:
          d1=float(input("Indique la primera diagonal de la figura:"))
          d2=float(input("indique la segunda diagonal de la figura: "))
          print(area_rombo(d1,d2))
      elif a==4:
          r=float(input("Indique el radio de la figura: "))
          print(area_circulo(r))
      else:
          print("Opcion inválida. Elija una opción válida.")
          a=float(input("Seleccione una opción: "))
          continue
      i2=1
           