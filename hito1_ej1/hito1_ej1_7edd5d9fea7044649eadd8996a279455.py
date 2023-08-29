# Obtener las notas del usuario
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentacion (PP): "))

# Calcular el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el promedio final a dos decimales
promedio_final_redondeado = int(promedio_final * 100) / 100

# Imprimir el promedio final
print("El promedio final es:", promedio_final_redondeado)