# Solicitar las cuatro notas al usuario
PT = float(input("Ingresa la nota de Tareas: "))
PI = float(input("Ingresa la nota de Interrogaciones: "))
NE = float(input("Ingresa la nota de Examen: "))
PP = float(input("Ingresa la nota de Presentación: "))

# Calcula el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondea
promedio_final = round(promedio_final, 1)

# Imprimir el promedio final obtenido
print(f"El promedio final es: {promedio_final}")

