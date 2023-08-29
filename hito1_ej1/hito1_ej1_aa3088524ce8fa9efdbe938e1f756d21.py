#Nota final
#entrada
PT = float(input("Ingrese la nota de Tareas (0-100): "))
PI = float(input("Ingrese la nota de Interrogaciones (0-100): "))
NE = float(input("Ingrese la nota de Examen (0-100): "))
PP = float(input("Ingrese la nota de Presentación (0-100): "))

promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    # Imprimir el resultado redondeado a un decimal
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es: ",promedio_final_redondeado)
