#Nota final

pt=float(input("ingrese nota de tareas: "))
pi=float(input("ingrese nota de interrogaciones: "))
ne=float(input("ingrese nota de examen: "))
pp=float(input("ingrese nota de presentacion: "))

ponderacionpt= (pt*0.3)
ponderacionpi= (pi*0.3)
ponderacionne= (ne*0.3)
notapp= (pp*0.1)

resultado = (ponderacionpt + ponderacionpi + ponderacionne + notapp)

print (round (resultado,1))