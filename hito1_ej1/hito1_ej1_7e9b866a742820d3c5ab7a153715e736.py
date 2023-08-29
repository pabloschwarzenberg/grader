#Nota final
PT = float(input("ingrese promedio de tareas: "))
PI = float(input("ingrese nota de interrogaciones: "))
NE = float(input("ingrese nota de examen: "))
PP = float(input("ingrese nota de presentacion: "))

formula = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
print(" la nota final de la asignatura es: " , formula)