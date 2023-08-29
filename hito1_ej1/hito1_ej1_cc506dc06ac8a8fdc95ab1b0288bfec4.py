#Nota final
# Usuario digitará las notas
PT = float(input("Nota de las Tareas: "))
PI = float(input("Nota de las Interrogaciones: "))
NE = float(input("Nota del Examen: "))
PP = float(input("Nota de la Presentación: "))

# Promedio final
nota_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el promedio 
nota_final = round(nota_final, 1)

# El resultado
print("La nota promedio final es:", nota_final)      