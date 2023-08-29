#Nota final

tareas = float(input("Ingresa tu nota de tareas: "))
interrogaciones = float(input("Ingresa tu nota de interrogaciones: "))
examen = float(input("Ingresa tu nota de examen: "))
presentacion = float(input("Ingresa tu nota de presentación: "))


promedio_final = 0.3 * tareas + 0.3 * interrogaciones + 0.3 * examen + 0.1 * presentacion


print("Tu promedio final es:", round(promedio_final, 1))
