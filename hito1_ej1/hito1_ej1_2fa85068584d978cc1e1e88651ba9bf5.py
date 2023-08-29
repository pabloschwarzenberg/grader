#Nota final
# Obtener las notas desde el usuario
PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de la Presentación: "))

# Calcular el promedio final
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:",promedio)