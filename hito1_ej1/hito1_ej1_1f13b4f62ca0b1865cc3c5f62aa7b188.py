#Nota final
pt=float(input("ingrese nota tareas: "))
pi=float(input("ingrese nota interrogaciones: "))
ne=float(input("infrese nota de examen: "))
pp=float(input("ingrese nota de presentacion: "))

ponderacionpt= (pt*0.3)
ponderacionpi= (pi*0.3)
ponderacionne= (ne*0.3)
ponderacionpp= (pp*0.1)

resultado = (ponderacionpt+ponderacionpi+ponderacionne+ponderacionpp)

print(round(resultado,1))
