print("\nCalculadora de nota final\n")

PT=float(input("Indique su nota de tareas: "))
PI=float(input("Indique su nota de interrogaciones: "))
NE=float(input("Indique su nota de examen: "))
PP=float(input("Indique su nota de presentacion: "))

nota_final= (PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)
print("\nLa nota final de su ramo es: ",round(nota_final,3),"\n")