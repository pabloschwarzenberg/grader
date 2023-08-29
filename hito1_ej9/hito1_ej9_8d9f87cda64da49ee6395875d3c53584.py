#Sistema de Ecuaciones
a = int(input("Ingrese primer número de la primera ecuación:"))
b = int(input("Ingrese segundo número de la primera ecuación:"))
c = int(input("Ingrese tercer número de la primera ecuación:"))
d = int(input("Ingrese primer número de la segunda ecuación:"))
e = int(input("Ingrese segundo número de la segunda ecuación:"))
f = int(input("Ingrese tercer número de la segunda ecuación:"))

x = (((e*c)-(b*f))/((a*e)-(b*d)))
y = (((a*f)-(d*c))/((a*e)-(b*d)))

print("x=",x)
print("y=",y)