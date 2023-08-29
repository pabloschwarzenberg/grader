#Nota final
PT = float(input("Ingrese nota tarea: "))
PI = float(input("Ingrese nota interrogaciones: "))
NE = float(input("Ingrese nota examen: "))
PP = float(input("Ingrese nota presentacion: "))

PF = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("Promedio final es: ", round(PF, 1))