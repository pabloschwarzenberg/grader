#Nota final
PT=float(input("ingrese nota de tarea: "))
PI=float(input("ingrese nota de interrogaciones: "))
NE=float(input("ingrese nota de examen: "))
PP=float(input("ingrese nota de presentacion: "))

promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("el promedio final es:", promedio_final)