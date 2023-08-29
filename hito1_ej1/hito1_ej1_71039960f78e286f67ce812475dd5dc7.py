#Nota final
PT = float(input("Introduzca nota de tareas: "))
PI = float(input("Introduzca nota de interrogaciones: "))
NE = float(input("Introduzca nota de examen: "))
PP = float(input("Introduzca nota de presentacion: "))

formula = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print(round(formula, 1))