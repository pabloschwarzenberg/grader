#Nota final
#Entrada
PT = float(input("Ingrese promedio notas Tareas: "))
PI = float(input("Ingrese promedio notas Interrogaciones: "))
NE = float(input("Ingrese nota de Examen: "))
PP = float(input("Ingrese promedio Presentación: "))

#Procedimiento
Promedio_final = round((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP),1)
print("Su promedio final es: ", Promedio_final)