import math



def area_triangulo(base,altura):

  return (base*altura)/2



def area_rectangulo(base,altura):

  return base*altura



def area_rombo(diagonal1,diagonal2):

  return (diagonal1*diagonal2)/2



def area_circulo(radio):

  return math.pi*radio*radio



if __name__ == "__main__":

  opcion = input("Elija figura 1) Triangulo 2) Rectangulo 3) Rombo 4) Circulo")

  if opcion == "1":

   b = eval(input("Ingrese la base del triangulo"))

   h = eval(input("Ingrese la altura del triangulo"))

   area = area_triangulo(b,h)

   print("El area del triangulo es : ", area)

  if opcion == "2":

   b = eval(input("Ingrese la base del rectangulo"))

   h = eval(input("Ingrese la altura del rectangulo"))

   area = area_rectangulo(b,h)

   print("El area del rectangulo es : ", area)

  if opcion == "3":

   d1 = eval(input("Ingrese la diagonal 1"))

   d2 = eval(input("Ingrese la diagonal 2"))

   area = area_rombo(d1, d2)

   print("El area del rombo es : ", area)

  if opcion == "4":

   r = eval(input("Ingrese el radio"))

   area = area_circulo(r)

   print("El area del circulo es : ", area)          