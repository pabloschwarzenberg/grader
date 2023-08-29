#Nota final
pt = float(input("Ingresa nota tareas:"))
pi = float(input("Ingresa nota interrogaciones:"))
ne = float(input("Ingresa nota examen:"))
pp = float(input("Ingresa nota presentacion:"))
promedio = 0.3 * pt + 0.3 * pi + 0.3 *ne + 0.1 * pp
promedior = round(promedio,1)
print(promedior)