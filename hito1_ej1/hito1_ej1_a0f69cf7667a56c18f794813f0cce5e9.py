#Nota final
      # Pedir al usuario que ingrese las cuatro notas
nota_PT = float(input("Ingrese la nota de PT (Tareas): "))
nota_PI = float(input("Ingrese la nota de PI (Interrogaciones): "))
nota_NE = float(input("Ingrese la nota de NE (Examen): "))
nota_PP = float(input("Ingrese la nota de PP (Presentación): "))

# Calcular el promedio final
promedio_final = 0.3 * nota_PT + 0.3 * nota_PI + 0.3 * nota_NE + 0.1 * nota_PP

# Redondear el promedio final a un decimal
promedio_final = round(promedio_final, 1)

# Imprimir el promedio final
print("El promedio final es:", promedio_final)