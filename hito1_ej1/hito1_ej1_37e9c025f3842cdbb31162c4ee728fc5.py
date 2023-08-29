PT = float(input("Indique la nota de tareas(PT): "))
PI = float(input("Indique la nota de interrogaciones(PI): "))
NE = float(input("Indique la nota de examen(NE): "))
PP = float(input("Indique la nota de examen(PP): "))

NF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
NF=round(NF, 1)

print("Nota final: ", NF)