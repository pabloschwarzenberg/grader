import math

def area_triangulo(base,altura):
    A=(base*altura)/2
    return A

def area_rectangulo(base,altura):
    B=(base*altura)
    return B

def area_rombo(diagonal1,diagonal2):
    C=(diagonal1*diagonal2)/2
    return C
def area_circulo(radio):
    Ci=math.pi*(radio**2)
    return Ci

if __name__ == "__main__":

  name=int(input("El area de que figura desea calcular:\n"
        "1)Triangulo\n"
        "2)Rectangulo\n"
        "3)Rombo\n"
        "4)Circulo\n"))
      
  if name == 1:
      base=int(input("base: "))
      altura=int(input("altura: "))
      triangulo = area_triangulo(base,altura)
      print(triangulo)
  if name == 2:
      base=int(input("base: "))
      altura=int(input("altura: "))
      rectangulo = area_rectangulo(base,altura)
      print(rectangulo)
  if name == 3:
      diagonal1=int(input("diagonal1: "))
      diagonal2=int(input("diagonal2: "))
      rombo = area_rombo(diagonal1,diagonal2)
      print(rombo)
  if name == 4:
      radio=int(input("radio :"))
      circulo = area_circulo(radio)
      print(circulo)