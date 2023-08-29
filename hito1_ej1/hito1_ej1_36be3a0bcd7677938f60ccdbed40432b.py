#Nota final
PT = float(input("escribe tus notas de tareas: "))
PI = float(input("escribe tus notas de interrogaciones: "))
NE = float(input("escribe tu nota del examen: "))
PP = float(input("escribe tu nota de presentación: "))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print("tu nota final es de", round(PF, 1))      