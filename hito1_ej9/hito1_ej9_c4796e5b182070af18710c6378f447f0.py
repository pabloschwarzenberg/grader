#Sistema de Ecuaciones
a=float(input("Ingrese el número que acompaña a la X en la primera ecuación:"))
b=float(input("Ingrese el número que acompaña a la Y en la primera ecuación:"))
c=float(input("Ingrese el término independiente de la primera ecuación:"))
d=float(input("Ingrese el número que acompaña a la X en la segunda ecuación:"))
e=float(input("Ingrese el número que acompaña a la Y en la segunda ecuación:"))
f=float(input("Ingrese el término independiente de la segunda ecuación:"))

x=((b*f)-(e*c))/((b*d)-(e*a))
y=((a*f)-(d*c))/((a*e)-(b*d))

print("x=",x)
print("y=",y)

