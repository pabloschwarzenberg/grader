# Solicitar al usuario ingresar las cuatro notas
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentacion (PP): "))

# Calcular el promedio final utilizando la fórmula dada
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el promedio final a un decimal
promedio_final_redondeado = round(promedio_final, 1)

# Imprimir el resultado redondeado
print("El promedio final es:", promedio_final_redondeado)
