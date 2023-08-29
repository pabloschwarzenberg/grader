#Sistema de Ecuaciones
a = float(input("Ingrese valor: "))
b = float(input("Ingrese valor: "))
c = float(input("Ingrese valor: ")) 
d = float(input("Ingrese valor: "))
e = float(input("Ingrese valor: "))
f = float(input("Ingrese valor: "))

x = ((f*b)-(e*c))/((b*d)-(a*e))
y = ((f*a)-(d*c))/((e*a)-(d*b))
print("x="+str(x))
print("y="+str(y))
      