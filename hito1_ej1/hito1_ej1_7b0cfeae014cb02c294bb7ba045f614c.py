#Nota final
PT = float(input("inserte su nota de las tareas: "))
PI = float(input("inserte su nota de interrogaciones: "))
NE = float(input("inserte su nota de examen: "))
PP = float(input("inserte su nota de presentacion: "))

print(round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1))