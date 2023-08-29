#Nota final
PT = float(input("ponga  la nota de tareas"))
PI = float(input("ponga la nota de interrogaciones"))
NE = float(input("ponga la nota de examen"))
PP = float(input("ponga la nota de presentacion"))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

round(PF,1)

print("Su promedio final es:", PF)