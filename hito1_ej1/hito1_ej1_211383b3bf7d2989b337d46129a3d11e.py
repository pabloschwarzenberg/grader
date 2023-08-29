# Solicitar al usuario las cuatro notas
PT = float(input("Ingresa la nota de Tareas (PT): "))
PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
NE = float(input("Ingresa la nota de Examen (NE): "))
PP = float(input("Ingresa la nota de Presentacion (PP): "))

# Calcular el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprimir el resultado redondeado a un decimal
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)
