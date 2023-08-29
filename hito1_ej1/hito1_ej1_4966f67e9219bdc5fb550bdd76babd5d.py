#Nota final
PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentacion: "))

promedio_final = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP) 
print("Su promedio final es: ", round(promedio_final, 1))