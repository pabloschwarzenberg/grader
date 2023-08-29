import math

def area_triangulo(base,altura):   
    area= base* altura/2
    return area

def area_rectangulo(base,altura):  
    area= base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area= diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area= math.pi*radio*radio
    return area
if __name__ == "__main__":
 while True:
  print("(1)Triangulo")
  print("(2)Rectangulo")
  print("(3)Rombo")
  print("(4)Circulo")
  print("(5)Salir")
  menu= int(input("Indique la figura la cual desea calcularle el área:"))

  if menu ==1:
    base= float(input("Indique la base del triangulo:"))
    altura= float(input("Indique la altura del triangulo:"))
    print("El area de la figura es:",area_triangulo(base,altura))

  elif menu ==2:
    base= float(input("Indique la base del rectangulo:"))
    altura= float(input("Indique la altura del rectangulo:"))
    print("El area de la figura es:",area_rectangulo(base,altura))
  elif menu ==3:
    diag1= float(input("Indique la diagonal 1:"))
    diag2= float(input("Indique la diagonal 2:"))
    print("El area de la figura es:",area_rombo(diag1,diag2))
  elif menu ==4:
    radio= float(input("indique el radio:"))
    print("El area de la figura es:",area_circulo(radio))
  elif menu ==5:
     print("Adios :)")
     break
  else:
     print("Ingrese una opción válida")
           