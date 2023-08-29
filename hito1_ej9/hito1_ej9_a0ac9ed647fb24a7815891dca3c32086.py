#Sistema de Ecuaciones
a = float(input("Ingrese un valor para ax: "))
b = float(input("Ingrese un valor para by: "))
c = float(input("Ingrese un valor para c: "))
#segunda ecuacion
d = float(input("Ingrese un valor para dx: "))
e = float(input("Ingrese un valor para ey: "))
f = float(input("Ingrese un valor para f: "))

#operacion
discriminante = a * e - b * d

sol_x = (c * e - b *f) / discriminante
sol_y = (a * f - c *d) / discriminante

print("x=",sol_x)
print("y=",sol_y)
