#Nota final
# Pedir las cuatro notas al usuario
PT = float(input("Ingresa la nota de Tareas: "))
PI = float(input("Ingresa la nota de Interrogaciones: "))
NE = float(input("Ingresa la nota de Examen: "))
PP = float(input("Ingresa la nota de Presentación: "))

# Calcular el promedio final
promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", round(promedio_final, 1))      