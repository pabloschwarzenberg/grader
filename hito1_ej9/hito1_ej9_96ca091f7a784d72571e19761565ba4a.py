#Sistema de Ecuaciones
a1=int(input("ingrese a1"))
b1=int(input("ingrese b1"))
c1=int(input("ingrese c1"))
a2=int(input("ingrese a2"))
b2=int(input("ingrese b2"))
c2=int(input("ingrese c2"))
determinante=a1*b2-b1*a2
if determinante !=0:
  x=(c1*b2-b1*c2)/determinante
  y=(a1*c2-c1*a2)/determinante
print("x=",round(x,1))
print("y=",round(y,1))