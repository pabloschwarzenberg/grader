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
  print("Calculadora geométrica \n 1 para area del triangulo \n 2 para area del rectangulo \n 3 para area del rombo \n 4 para area del circulo")
  opcion = 6
  while opcion != 0:
    opcion = int(input("Escoja un numero"))
    if opcion == 1:
        print("Escogió Área del Triangulo")
        base = int(input("Ingrese base: "))
        altura = int(input("Ingrese altura: "))
        print("Area: {}".format(area_triangulo(base,altura)))
    elif opcion ==2:
        print("Escogió Área del Rectángulo")
        b = int(input("Ingrese Lado 1: "))
        a = int(input("Ingrese Lado 2: "))
        print("Area: {}".format(area_rectangulo(b,a)))
    elif opcion ==3:
        print("Escogió Área del Rombo")
        d1 = int(input("Ingrese Diagonal 1: "))
        d2 = int(input("Ingrese Diagonal 2: "))
        print("Area: {}".format(area_rombo(d1,d2)))
    elif opcion ==4:
        print("Escogió Área del Circulo")
        r = int(input("Ingrese el radio: "))
        print("Area: {}".format(area_circulo(r))) 