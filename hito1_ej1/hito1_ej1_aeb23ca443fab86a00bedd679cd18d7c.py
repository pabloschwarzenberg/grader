pt=0.0
pi=0.0
ne=0.0
pp=0.0
nf=0.0
pt=float(input("Ingrese promedio tareas: "))
pi=float(input("Ingrese notas de interrogaciones: "))
ne=float(input("Ingrese nota de examen : "))
pp=float(input("Ingrese nota de presentacion :"))

nf=(pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1)
nf1= round(nf, 1)

print("Su nota final es:",nf1)