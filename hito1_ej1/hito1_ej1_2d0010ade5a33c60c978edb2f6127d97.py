#Nota final
pt = float(input("ingrese sus notas de tarea: "))
pi = float(input("ingrese sus notas de interrogaciones: "))
ne = float(input("ingrese sus nootas de examen: "))
pp = float(input("ingrese sus notas de presentacion: "))
promediof = pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1
promedior = round(promediof,1)
print("el promedio de las cuatro notas es:", promedior)       