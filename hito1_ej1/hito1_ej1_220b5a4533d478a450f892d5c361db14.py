#Nota final
pt = float(input("Ingrese su nota de tareas :"))
pi = float(input("Ingrese su nota de interrograciones :"))
ne = float(input("Ingrese su nota de examen :"))
pp = float(input("Ingrese su nota de presentacion :"))

a=float(0.3*pt)
b=float(0.3*pi) 
c=float(0.3*ne)
d=float(0.1*pp)
x=float(a+b+c+d)
print("el promedio es:" "{0:.1f}".format(x))