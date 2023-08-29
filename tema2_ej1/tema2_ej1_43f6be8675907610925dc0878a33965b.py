import math
def area_triangulo(base,altura):
    a=base*altura
    b=a/2
    return b

def area_rectangulo(base,altura):
    a=base*altura
    return a

def area_rombo(diagonal1,diagonal2):
    a=diagonal1*diagonal2
    b=a/2
    return b

def area_circulo(radio):
    b=math.pi
    c=radio*radio
    a=c*b
    return a
if __name__ == "__main__":
  opcion = 0
  print("(1)Calcular Area de un Triangulo\n(2)Calcular Area de un rectangulo\n(3)Calcular area de un rombo\n(4)Calcular el area de un circulo")
  opcion=int(input("¿Que Quiere hacer?"))
  if opcion==1:
      base=int(input("Ingrese la base del triangulo"))
      altura=int(input("Ingrese la altura del triangulo"))
      a=area_triangulo(base,altura)
      print("el area del triangulo es,",a)
  if opcion==2:
      base=int(input("Ingrese la base del rectangulo"))
      altura=int(input("Ingrese la altura del rectangulo"))
      a=area_rectangulo(base,altura)
      print("el area del rectangulo es,",a)
  if opcion==3:
      diagonal1=int(input("Ingrese la diagonal 1 del rombo"))
      diagonal2=int(input("Ingrese la diagonal 2 del rombo"))
      a=area_rombo(diagonal1,diagonal2)
      print("el area del triangulo es,",a)
  if opcion==4:
      radio=int(input("Ingrese el radio del circulo"))
      a=area_circulo(radio)
      print("el area del circulo es,",a)

           