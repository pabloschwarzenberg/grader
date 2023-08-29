PT = float(input("Ingrese su nota de Tareas: "))
PI = float(input("Ingrese su nota de Interrogaciones: "))
NE = float(input("Ingrese su nota del examen: "))
PP = float(input("Ingrese su nota de Presentacion: "))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
PFR = round(PF, 1)
print("", PFR)