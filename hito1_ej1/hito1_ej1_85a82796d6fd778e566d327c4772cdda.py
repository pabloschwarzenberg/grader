#Nota final
 # Solicitar las notas al usuario
nota_PT = float(input("Ingrese la nota de Tareas: "))
nota_PI = float(input("Ingrese la nota de Interrogaciones: "))
nota_NE = float(input("Ingrese la nota de Examen: "))
nota_PP = float(input("Ingrese la nota de Presentación: "))

# Calcular el promedio final
promedio_final = 0.3 * nota_PT + 0.3 * nota_PI + 0.3 * nota_NE + 0.1 * nota_PP

# Imprimir el resultado redondeado a un decimal
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)
     