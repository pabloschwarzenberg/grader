#Nota final
PT=float(input("ingrese notas de tareas: "))

PI=float(input("ingrese notas de interrogaciones: "))

NE=float(input("ingrese notas del examen: "))

PP=float(input("ingrese nota de presentacion:"))

nt = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
round(nt, 1)
print("la nota final es:" + str(nt))   