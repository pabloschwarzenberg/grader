print("¿Quiere sacar el area de que figura")
print("1= Circulo")
print("2=rectanculo")
print("3=Tiangulo")
print("4=Rombo")
import math
def area_circulo(a):
          A=math.pi*a**2
          return(A)
          
def area_rectangulo(a,b):
          A=a*b
          return (A)
         
def area_triangulo(a,b):
          A=(a*b)/2
          return (A)
   
def area_rombo(a,b):
          A=(a*b)/2
          return (A)
if __name__=='__main__':
  c=int(input("Ingrese el número de la figura qui quiere calcular el área"))
  if c==1:
      a=int(input("Ingrese el radio de la esfera"))
      print("El area de la esfera es:",area_circulo(a))

  elif c==2:
      b=int(input("Ingrese los lados del rectangulo"))
      print("El area del rectangulo es:",area_rectangulo(a,b))

  elif c==3:
      a=int(input("Ingrese la base del triangulo"))
      d=int(input("Ingrese la altura del triangulo"))
      print("El area del triangulo es:",area_triangulo(a,d))

  elif c==4:
      a=int(input("Ingrese la primera diagonal"))
      d=int(input("Ingrese la segunda diagonal"))
      print("El area del rombo es:",area_rombo(a,d))
