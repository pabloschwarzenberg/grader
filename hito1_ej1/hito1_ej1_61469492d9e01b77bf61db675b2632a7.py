#Nota final
pt=float(input("ingresar nota de tareas: "))
pi=float(input("ingresar nota de interrogaciones: "))
ne=float(input("ingresar nota de examen: "))
pp=float (input("ingresar nota de presentacion: "))

ponderacionpt= (pt*0.3)
ponderacionpi= (pi*0.3)
ponderacionne= (ne*0.3)
notapresentacion= (pp*0.1)

resultado= (ponderacionpt+ponderacionpi+ponderacionne+notapresentacion)

print (round(resultado,1))