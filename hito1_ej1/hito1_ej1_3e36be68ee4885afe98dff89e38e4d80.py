#Nota final
print("Hola alumn@, a continuación ingrese las notas correspondientes a lo que se le pida:")
PT=str(input(print("Nota tareas: ")))
PI=str(input(print("Nota interrogaciones: ")))
NE=str(input(print("Nota Exámen: ")))
PP=str(input(print("Nota presentación: ")))

nota_final= (float(PT) * 0.3) + (float(PI) * 0.3) + (float(NE) * 0.3) + (float(PP) * 0.1)
redondeado=round(nota_final, 1)
print("El promedio final de sus notas es de:", redondeado)