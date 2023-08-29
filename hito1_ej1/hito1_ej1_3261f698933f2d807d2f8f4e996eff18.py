#Nota final
print("ingrese notas")
PT=float(input("Ingrese la nota de tareas: "))
PI=float(input("Ingrese la nota interrogaciones: "))
NE=float(input("Ingrese la nota del examen: "))
PP=float(input("Ingrese la nota de la presentacion: "))
PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
PFR = round(PF, 2)
print("el promedio final es: ", PFR)     