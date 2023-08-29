#Nota final
PT = float(input("Ingresar nota tareas: "))
PI = float(input("Ingresar notas interrogaciones: "))
NE = float(input("Ingresar notas examen: "))
PP = float(input("Ingresar notas presentacion: "))

NT = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print(round(NT, 1))