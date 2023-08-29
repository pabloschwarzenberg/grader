import math
def area_triangulo(b,a):
    a2=(a*b)/2
    return a2
    
def area_rectangulo(b,a):
    a1=a*b
    return a1

def area_rombo(d,D):
    a3=D*d/2
    return a3

def area_circulo(r):
    a4=math.pi*(r**2)
    return a4

if __name__ == "__main__":
  print("Area de las figuras, 1:rectangulo, 2:triangulo, 3:rombo y 4:circulo")
  f=int(input("Ingrese el numero de la figura: "))
  if f==1:
    b=float(input("Ingrese base: "))
    a=float(input("Ingrese altura: "))
    print(area_rectangulo(b,a))
  elif f==2:
    b=float(input("Ingrese base: "))
    a=float(input("Ingrese altura: "))
    print(area_triangulo(b,a))
  elif f==3:
     d=float(input("Ingrese diagonal menor: "))
     D=float(input("Ingrese diagonal mayor: "))
     print(area_rombo(d,D))
  elif f==4:
    r=float(input("Ingrese el radio: "))
    print(area_circulo(r))
  
           