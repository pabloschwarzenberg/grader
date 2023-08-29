#Nota final
PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de interrogaciones: ")) 
NE = float(input("ingrese nota de Examen: "))
PP = float(input("ingrese nota de presentación: "))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
PF = round(PF, 1)

print(PF)