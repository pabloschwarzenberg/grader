#Nota final
PT = float(input("ingrese nota tareas: "))
PI = float(input("ingrese nota interrogaciones: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentacion: "))

promedio_notas = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promedio_notas,1))