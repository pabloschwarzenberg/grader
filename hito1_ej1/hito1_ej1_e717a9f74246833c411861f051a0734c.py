#Nota final
PT=float(input("ingrese nota de tareas"))
PI=float(input("ingrese nota de interrogaciones"))
NE=float(input("ingrese nota de examen"))
PP=float(input("ingresa de nota de presentacion"))
nota_final= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("promedio final:", round(nota_final,1))