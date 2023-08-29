#Nota final
PT=float(input("Ingrese nota de las tareas:"))
PI=float(input("Ingrese nota de las interrogaciones:"))
NE=float(input("Ingrese nota de los examenes:"))
PP=float(input("Ingrese nota de la nota de presentacion:"))

nota_final=0.3*PT+0.3*PI+0.3*NE+0.1*PP
NFA=round(nota_final,1)

print(NFA)