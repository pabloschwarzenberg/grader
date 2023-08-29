#Nota final
PT = float(input("Ingrese la nota de Tareas (0-10): "))
PI = float(input("Ingrese la nota de Interrogaciones (0-10): "))
NE = float(input("Ingrese la nota de Examen (0-10): "))
PP = float(input("Ingrese la nota de Presentación (0-10): "))

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("El promedio final es:", round(promedio, 1))