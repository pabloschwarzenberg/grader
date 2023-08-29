#Nota final
nota_tareas = float(input("Ingrese la nota de Tareas (PT): "))
nota_interrogaciones = float(input("Ingrese la nota de Interrogaciones (PI): "))
nota_examen = float(input("Ingrese la nota de Examen (NE): "))
nota_presentacion = float(input("Ingrese la nota de Presentación (PP): "))

promedio_final = 0.3 * nota_tareas + 0.3 * nota_interrogaciones + 0.3 * nota_examen + 0.1 * nota_presentacion
promedio_redondeado = round(promedio_final, 1)

print("El promedio final es:", promedio_redondeado)





 