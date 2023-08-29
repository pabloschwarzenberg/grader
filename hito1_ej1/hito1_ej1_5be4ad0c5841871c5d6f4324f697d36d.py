nota_PT = float(input("Ingrese la nota de las Tareas: "))
nota_PI = float(input("Ingrese la nota de las Interrogaciones: "))
nota_NE = float(input("Ingrese la nota del Examen: "))
nota_PP = float(input("Ingrese la nota de la Presentación: "))
promedio_final = 0.3 * nota_PT + 0.3 * nota_PI + 0.3 * nota_NE + 0.1 * nota_PP
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)