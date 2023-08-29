#Sistema de Ecuaciones
a=float(input("Ingrese"))
b=float(input("Ingrese"))
c=float(input("Ingrese"))
d=float(input("Ingrese"))
e=float(input("Ingrese"))
f=float(input("Ingrese"))

determinante=a*e-b*d
if determinante!=0:
      x=(c*e-b*f)/determinante
      x=round(x,1)
      y=(a*f-c*d)/determinante
      y=round(y,1)
      print("x=",x,"y=",y)
else:
      print("El sistema no tiene solución")      