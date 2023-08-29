#Nota final
# Solicitar las cuatro notas al usuario
nota_PT = float(input("Ingrese la nota de las Tareas (PT): "))
nota_PI = float(input("Ingrese la nota de las Interrogaciones (PI): "))
nota_NE = float(input("Ingrese la nota del Examen (NE): "))
nota_PP = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular el promedio final
promedio_final = 0.3 * nota_PT + 0.3 * nota_PI + 0.3 * nota_NE + 0.1 * nota_PP

# Imprimir el resultado redondeado a un decimal
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)
  