#Nota final
pt = float(input("Ingrese nota tareas: "))
pi = float(input("Ingrese nota interrogaciones: "))
ne = float(input("Ingrese nota examenes: "))
pp = float(input("Ingrese nota presentacion: "))
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

print(round(promedio,1))
     