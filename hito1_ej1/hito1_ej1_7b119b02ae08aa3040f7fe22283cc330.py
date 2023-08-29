#Nota final
# Pedimos las cuatro notas al usuario
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentación: "))

# Calculamos el promedio final
promedio = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)

# Redondeamos el resultado a dos decimales
promedio = round(promedio, 2)

# Imprimimos el resultado
print("El promedio final es:", promedio)      