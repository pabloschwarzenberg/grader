#Nota final
PT = float(input("Introducir nota de tareas"))
PI = float(input("Introducir nota de Controles"))
NE = float(input("Introducir nota de examen"))
PP = float(input("Introducir nota de presentacion"))
PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

round(PF,1)

print("Su promedio final es:", PF)      