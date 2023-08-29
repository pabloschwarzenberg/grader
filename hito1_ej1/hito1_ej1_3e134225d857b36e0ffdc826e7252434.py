#Nota final
nota_pt=float(input("Ingrese nota de tareas: "))
nota_pi=float(input("Ingrese nota de interrogaciones: "))
nota_ne=float(input("Ingrese nota de examen: "))
nota_pp=float(input("Ingrese nota de presentación: "))
nota_final=(0.3*nota_pt) + (0.3*nota_pi) + (0.3*nota_ne) + (0.1*nota_pp)
redondeado=round(nota_final,1)
print(redondeado)