
import math

def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2)/2

def area_circulo(radio):
    return (radio * radio) * math.pi
if __name__ == "__main__":
  import math
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2)/2

def area_circulo(radio):
    return (radio * radio) * math.pi
if __name__ == "__main__":
  print("Calculadora geométrica") 
  print("1.Area del triangulo")
  print("2.Area del rectangulo")
  print("3.Area del rombo")
  print("4.Area del circulo")
   
  opcion = 0
  while opcion != 5:
    opcion = int(input("Elija opcion"))
    if opcion == 1:
        print("Área Triangulo")
        base = int(input("Ingrese base: "))
        altura = int(input("Ingrese altura: "))
        print("Area: {}".format(area_triangulo(base,altura)))
    elif opcion ==2:
        print("Área del Rectángulo")
        b = int(input("Ingrese Lado 1: "))
        a = int(input("Ingrese Lado 2: "))
        print("Area: {}".format(area_rectangulo(b,a)))
    elif opcion ==3:
        print("Área del Rombo")
        d1 = int(input("Ingrese Diagonal 1: "))
        d2 = int(input("Ingrese Diagonal 2: "))
        print("Area: {}".format(area_rombo(d1,d2)))
    elif opcion ==4:
        print("Área del Circulo")
        r = int(input("Ingrese el radio: "))
        print("Area: {}".format(area_circulo(r))) 