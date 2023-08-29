#Nota final
PT = float(input("Escriba Nota promedio de Tareas: "))
PI = float(input("Escriba Nota promedio de Interrogaciones: "))
NE = float(input("Escriba Nota de Examen: "))
PP = float(input("Escriba Nota de Presentación: "))

notafinal = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La nota final del alumno es: ",round(notafinal, 1))