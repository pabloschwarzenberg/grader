 #funciones   
import math              
def area_rectangulo(base,altura):
    return float((base)*(altura))
def area_triangulo(base,altura):
    return float(((base)*(altura))/2)
def area_circulo(radio):
    return float(((radio)**2)*math.pi)
def area_rombo(diagonal1,diagonal2):
    return float(((diagonal1)*(diagonal2))/2)

if __name__ == "__main__":
  while True:
      print("Bienvenido a la increible calculadora geométrica de la vida.¿Qué desea calcular?")
      print("0:triángulo")
      print("1:rombo")
      print("2:circulo")
      print("3:rectangulo")

      respuesta=int(input())
      figuras=["triangulo","rombo","circulo","rectangulo"]
      print("Usted ha escogido calcular el area de un {0}".format(figuras[respuesta]))
      print("Ingrese los datos necesarios")
      if respuesta==0:
          base=int(input("base: "))
          altura=int(input("altura: "))
          print("El valor del area del triangulo es:",area_triangulo(base,altura))

      if respuesta==1:
          diagonal1=int(input("diagonal 1: "))
          diagonal2=int(input("diagonal 2: "))
          print("El valor del area del rombo es:",area_rombo(diagonal1,diagonal2))

      if respuesta==2:
          radio=int(input("radio: "))
          print("El valor del area del circulo es:",area_circulo(radio))

      if respuesta==3:
          base=int(input("base: "))
          altura=int(input("altura: "))
          print("El valor del area del rectangulo es:",area_rectangulo(base,altura))

      respuesta2=input("¿Desea calcular algo más?")
      if respuesta=="no":
          print("Adios")
          break
      else:
          pass

           