#Nota final

pt = float(input("ingrese la nota de tareas: "))
pi = float(input("ingrese la nota de interrogaciones: "))
ne = float(input("ingrese la nota de examen: "))
pp = float(input("ingrese la nota de presentacion: "))



ponderacionpt= (pt*0.3)
ponderacionpi= (pi*0.3)
ponderacionne= (ne*0.3)
notapresentacion= (pp*0.1)

resultado=(ponderacionpt + ponderacionpi + ponderacionne + notapresentacion)

print(round(resultado,1))