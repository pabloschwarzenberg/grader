#Sistema de Ecuaciones

def sistema_ecuaciones (a,b,c,d,e,f):
  determinante= a*e - b*d
  if determinante!=0:
    x=(c*e-b*f)/determinante
    y=(a*f-c*d)/determinante
    return x,y
  else:
    return None, None

a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
c=float(input("Ingrese c: "))
d=float(input("Ingrese d: "))
e=float(input("Ingrese e: "))
f=float(input("Ingrese f: "))

x=(sistema_ecuaciones(a, b, c, d, e, f)[0])
y=(sistema_ecuaciones(a, b, c, d, e, f)[1])
x=(round(x,1))
y=(round(y,1))

print("[","\'x=",x,"\'","\'y=",y,"\'","]")