#Nota final

#ingresar las notas con un punto(.) en vez de una coma(,)
pt=float(input("nota de tareas: "))
pi=float(input("nota de interrogaciones: "))
ne=float(input("nota de examen: "))
pp=float(input("nota de presentacion: "))

prom=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print("el promedio final es: ",(prom))