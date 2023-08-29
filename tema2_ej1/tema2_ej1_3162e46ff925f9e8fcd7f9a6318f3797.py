def area_triangulo(base,altura):
 atriangulo=((base*altura)/2)
 return print ("El area calculada es : ",atriangulo)
def area_rectangulo(a,b):
 arectangulo= a*b
 return print ("El area calculada es :",arectangulo)
def area_rombo(diagonal1,diagonal2):
  arombo=((diagonal1*diagonal2)/2)
  return print ("El area calculada es; ",arombo)
def area_circulo(radio):
 import math
 acirculo= (math.pi*(radio*radio))
 return print ("el area calculada es : ",acirculo)
print("Calcular Áreas de figuras Geométricas.\n")
print("1.Triángulo.\n2.Rectángulo.\n3.Rombo.\n4.Circulo.")
if __name__ == "__main__":
 f=int(input("Ingrese el numero de la figura geometrica que desea calcular: "))
 if f ==1:
  area_triangulo((int(input("Ingrese el valor de la base del triangulo: "))),(int(input("Ingrese el valor de la altura del triangulo: "))))
 elif f ==2:
  area_rectangulo(int(input("Inserte la base: ")),int(input("Inserte la altura : ")))
 elif f ==3:
  area_rombo(int(input("Inserte la diagonal1: ")),int(input("Inserte la diagonal2: ")))
 elif f ==4 :
  area_circulo(int(input("Inserte el radio: ")))
           