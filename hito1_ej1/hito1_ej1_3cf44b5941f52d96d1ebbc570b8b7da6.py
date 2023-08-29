# Nota final
# Inicio
PT = float(input('Ingrese nota de tarea: '))
PI = float(input('Ingrese nota de interrogación: '))
NE = float(input('Ingrese nota de examen: '))
PP = float(input('Ingrese nota de presentación: '))
# Proceso
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_final = round(promedio_final, 2)  # Redondear a dos decimales
# Salida
print('La nota final es:', promedio_final)