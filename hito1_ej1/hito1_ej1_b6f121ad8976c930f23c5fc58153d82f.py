#Nota final
# Se solicitan las cuatro notas al usuario
nota_tareas = float(input("Ingrese la nota de Tareas: "))
nota_interrogaciones = float(input("Ingrese la nota de Interrogaciones: "))
nota_examen = float(input("Ingrese la nota de Examen: "))
nota_presentacion = float(input("Ingrese la nota de Presentación: "))

# Se calcula el promedio final utilizando la fórmula
promedio_final = 0.3 * nota_tareas + 0.3 * nota_interrogaciones + 0.3 * nota_examen + 0.1 * nota_presentacion

# Se redondea el promedio final a un decimal
promedio_final_redondeado = round(promedio_final, 1)

# Se imprime el promedio final redondeado
print("El promedio final es:", promedio_final_redondeado)
  