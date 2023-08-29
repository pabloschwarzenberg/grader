#Nota final
PT = float(input("ingresar nota tarea: "))
PI = float(input("ingresar nota de interrogaciones: "))
NE = float(input("ingresar nota de examen: "))
PP = float(input("ingresar nota de presentacion: "))
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promedio, 2))