#Nota final
pt = eval(input("Ingrese nota de tarea: "))
pi = eval(input("Ingrese nota de interrogaciones: "))
ne = eval(input("Ingrese nota de examen: "))
pp = eval(input("Ingrese nota de presentacion: "))

notafin=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print(round(notafin,1))     