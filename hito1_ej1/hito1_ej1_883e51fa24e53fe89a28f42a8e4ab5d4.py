# Pedimos las cuatro notas al usuario
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentación: "))

# Calculamos el promedio final con la fórmula proporcionada
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

# Redondeamos el promedio final a un decimal
promedio_final_redondeado = round(promedio_final, 1)

# Imprimimos el promedio final redondeado
print("El promedio final es:", promedio_final_redondeado)
      