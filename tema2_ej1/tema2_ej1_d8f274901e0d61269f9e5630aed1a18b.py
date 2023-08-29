import math

#Funcion triangulo
def area_triangulo(base,altura):
    formula_a = (base * altura)/2
    return formula_a
    pass

#Funcion rectangulo
def area_rectangulo(base,altura):
    formula_b = (base * altura)
    return formula_b
    pass

#Funcion rombo
def area_rombo(diagonal1,diagonal2):
    formula_c = (diagonal1 * diagonal2)/2
    return formula_c
    pass

#Funcion circulo
#MATH.PI
def area_circulo(radio):
    formula_d = (radio * radio)*math.pi
    return formula_d
    pass

#Interfaz

if __name__ == "__main__":
  print("Seleccione la opcion")
  print("Opcion 1: Area de un triangulo")
  print("Opcion 2: Area de un rectangulo")
  print("Opcion 3: Area de un rombo")
  print("Opcion 4: Area de un circulo")

  x = int(input("Seleccione la opcion: "))

  if x == 1:
    a = float(input("Digite la base del triangulo: "))
    b = float(input("Digite la altura del triangulo: "))
    resultado = area_triangulo(a,b)

  if x == 2:
    a = float(input("Digite la base del rectangulo: "))
    b = float(input("Digite la altura del rectangulo: "))
    resultado = area_rectangulo(a,b)

  if x == 3:
    a = float(input("Digite la primera diagonal del rombo: "))
    b = float(input("Digite la segunda diagonal del rombo: "))
    resultado = area_rombo(a,b)

  if x == 4:
    a = float(input("Digite el radio del circulo: "))
    resultado = area_circulo(a)

  print("El resultado es:",resultado)  
  pass
           