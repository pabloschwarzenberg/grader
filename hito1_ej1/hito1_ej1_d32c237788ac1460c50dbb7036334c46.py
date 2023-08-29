#Nota final

# Solicitar las notas al usuario
tareas = float(input("Ingrese la nota de Tareas: "))
interrogaciones = float(input("Ingrese la nota de Interrogaciones: "))
examen = float(input("Ingrese la nota de Examen: "))
presentacion = float(input("Ingrese la nota de Presentacion: "))

# Calcular la nota final
nota_final = 0.3 * tareas + 0.3 * interrogaciones + 0.3 * examen + 0.1 * presentacion

# Imprimir el resultado redondeado a un decimal
print("La nota final es:", round(nota_final, 1))