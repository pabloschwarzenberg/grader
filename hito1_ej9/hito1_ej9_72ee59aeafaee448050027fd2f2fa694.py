#Sistema de Ecuaciones
a=float(input("ingresa a: "))
b=float(input("ingresa b: "))
c=float(input("ingresa c: "))
d=float(input("ingresa d: "))
e=float(input("ingresa e: "))
f=float(input("ingresa f: "))


y=(c*d-a*f)/(b*d-a*e)
x=(f-e*y)/d

print("x= ",x)
print("y= ",y)
      