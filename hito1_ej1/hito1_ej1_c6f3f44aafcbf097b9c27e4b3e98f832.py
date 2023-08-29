#Nota final
PT = float(input("ponga nota de tarea"))
PI = float(input("ponga nota de interrogaciones"))
PE = float(input("ponga nota de examen"))
PP = float(input("ponga nota de presentacion"))

PF = 0.3 * PT + 0.3 * PI + 0.3 * PE + 0.1 * PP
round(PF,1)

print(PF)      