#Nota final
# Solicitar las notas al usuario
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentación: "))

# Calcular el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el promedio final a un decimal
promedio_final_redondeado = round(promedio_final, 1)

# Imprimir el resultado
print("El promedio final es:", promedio_final_redondeado)
  