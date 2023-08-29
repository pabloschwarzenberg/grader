#Nota final
pt = float(input(" ingresar nota de tareas: "))
pi = float(input(" ingresar nota de interrogaciones: "))
ne = float(input(" ingresar nota de examen:"))
pp = float(input(" ingresar nota de presentacion: "))

promediopt= (pt*0.3)
promediopi= (pi*0.3)
promedione= (ne*0.3)
notapresentacion= (pp*0.1)

resultado= (promediopt + promediopi + promedione + notapresentacion)

print(round(resultado, 1))