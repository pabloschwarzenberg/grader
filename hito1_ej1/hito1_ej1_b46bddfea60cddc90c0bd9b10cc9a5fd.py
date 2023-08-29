#Nota final
pt=float(input("Ingrese nota tareas: "))
pi=float(input("Ingrese nota interrogantes: "))
ne=float(input("Ingrese nota examen: "))
pp=float(input("Ingrese nota presentacion: "))

res=((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp))
print(round(res,1))      